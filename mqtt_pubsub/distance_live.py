import datetime as dt
import threading

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import paho.mqtt.client as paho


# Connection details
HOST = "172.27.28.18"
PORT = 1883
TIME_OUT = 60

# Topic and data
TOPIC = "sensors/dist_cm"


class LiveStream:
    def __init__(self) -> None:
        self.client = None
        self.xs = []
        self.ys = []

        stream = threading.Thread(target=self.subscriber)
        stream.start()

    def subscriber(self):
        # Create connection and register handler
        self.client = paho.Client()
        self.client.on_message = self.message_handler
        if self.client.connect(HOST, PORT, TIME_OUT):
            print('Connection failed!')
            exit(-1)

        # Subscribe to the topic
        self.client.subscribe(TOPIC)

        try:
            self.client.loop_forever()

        except KeyboardInterrupt as e:
            print('\nSTOP: Subscriber service.\n')
        finally:
            self.client.disconnect()

    def message_handler(self, client, user_data, msg):
        self.ys.append(float(msg.payload.decode()))
        self.xs.append(dt.datetime.now().strftime('%H:%M:%S'))

        print(f'Time: {self.ys[-1]}\t info: {self.xs[-1]}')


if __name__ == '__main__':
    plt.rcParams["figure.autolayout"] = True

    ls = LiveStream()

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    xs = []
    ys = []

    def animate(i, xs, ys):
        x = xs[-20:]
        y = ys[-20:]
        ax.clear()
        ax.plot(x, y, 'o-r')
        ax.set_ylim(0, 100)

        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('Distance over Time')
        plt.ylabel('Distance (CM)')
        plt.xlabel('Time (H:M:S)')

    animated_plot = animation.FuncAnimation(
        fig,
        animate,
        fargs=(ls.xs, ls.ys),
        interval=1000,
        cache_frame_data=False
    )

    # manager = plt.get_current_fig_manager()
    # manager.full_screen_toggle()
    plt.show()
    ls.client.disconnect()

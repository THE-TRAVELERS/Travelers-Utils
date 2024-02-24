from __future__ import print_function


from inputs import get_gamepad
import json


def main():
    """Just print out some event infomation when the gamepad is used."""
    my_dict = {}
    for i in range(500):
        events = get_gamepad()
        for event in events:
            if event.ev_type == "Key":
                print(f"{event.code} : {event.state}")
            if str(event.ev_type) in my_dict:
                my_dict[str(event.ev_type)] += [event.code]
            else:
                my_dict[str(event.ev_type)] = [event.code]
            my_dict[str(event.ev_type)] = list(set(my_dict[str(event.ev_type)]))
            if event.code in my_dict:
                my_dict[event.code] += [event.state]
            else:
                my_dict[event.code] = [event.state]

    with open("sample.json", "w") as outfile:
        json.dump(my_dict, outfile)


if __name__ == "__main__":
    main()

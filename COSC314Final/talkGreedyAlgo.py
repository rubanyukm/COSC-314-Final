# Programmed by Ruben Maidaniuc
# Programming project 9 on pg. 238 Chapter
# Written using Python 3.6.5
# Inputs should be entered like so: "Talk 0: 900 1100"

class Talks:

    def __init__(self, talk_name, talk_duration):
        self.talk_name = talk_name
        self.talk_duration = talk_duration

    def talkNum(self):
        setList = []
        numTalks = int(input("How many talks?: "))
        for i in range(numTalks):
            print("Talk %d: " % i, end="")
            start, end = map(int, input().split())
            setList.append((start, end))

        return setList

    def interval_scheduling(self, setList, talkList):
        setList.sort(key=lambda x: x[1])

        finish = 0

        for r in setList:
            if finish <= r[0]:
                finish = r[1]
                talkList.append(r)

        return talkList


if __name__ == "__main__":
    compatibleTalks = []
    talks = Talks("", "")
    talks.interval_scheduling(talks.talkNum(), compatibleTalks)

    print("The talks will be scheduled during these times: " + str(compatibleTalks))

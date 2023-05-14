# pip install emoji==1.7
from emoji import UNICODE_EMOJI

uni = UNICODE_EMOJI['en']


class mingle:
    def __init__(self, token):
        pass


class Foo(mingle):
    kw = {"일일호프": ["일일호프", "일홉"], "과잠": ["과잠"], "스터디": ["스터디", "공부"], "운동": ["운동", "체육", "스포츠"]}
    # kw2 = {"일정": ["일정", "일시", "날짜"], "장소": ["장소"]}
    kw2 = {"일정": "일정", "일시": "일정", "날짜": "일정", "장소": "장소", "위치": "장소", "입장료": "입장료", "이벤트": "이벤트", "": ""}

    targetkw = ["일일호프"]

    targetkw2 = ["일정", "장소", "입장료", "이벤트"]

    def convert_to_emoji(self, text):
        while True:
            i1 = -1;
            i2 = -1
            lentext = len(text)
            for i in range(lentext):
                ch = text[i]
                if ch == ':' and i1 < 0:
                    i1 = i
                elif ch == ' ' and i1 >= 0:
                    i1 = -1
                elif ch == ':' and i1 >= 0:
                    i2 = i + 1
                    break
            if i2 < 0:
                break
            text = text[:i1] + "💛" + text[i2:]
        return text

    def important(self, text):
        txt = text
        text = self.convert_to_emoji(text)
        target = []
        i1 = -1;  # i2=-1
        lentext = len(text)
        for i in range(lentext):
            ch = text[i]
            if i1 < 0 and (ch in uni):
                i1 = i
            elif i1 >= 0 and ch == text[i1]:
                target.append(text[i1 + 1:i])
                i1 = -1
        # print(target)
        return target

    def make_dict(self, text):
        target = self.important(text)
        result_dict = dict()
        for txt in target:
            txtsplit = txt.split(':')
            txt0 = "";
            txt1 = ""
            if len(txtsplit) == 1:
                txt1 = txtsplit[0].strip()
            if len(txtsplit) > 1:
                txt0 = txtsplit[0].strip()
                txt1 = txtsplit[1].lstrip()
            if txt0 in self.kw2:
                result_dict[self.kw2[txt0]] = txt1
            else:
                self.kw2[txt0] = txt0
                result_dict[self.kw2[txt0]] = txt1
                # result_dict[""] = txt1
        return result_dict

    def print(self, text):
        result_dict = self.make_dict(text)
        for i in result_dict:
            j = i
            if i == "":
                j = "비고"
            print(j, ':', result_dict[i])
        print()

    def is_needed(self, text):
        j = 0
        for kword in self.targetkw:
            c = 0
            kwlist = self.kw[kword]
            for i in kwlist:
                if i in text:
                    c = 1
                    break
            if c > 0:
                return j
            j += 1
        return -1

    def extract_keyword(self, all_text):
        result_text = []
        for text in all_text:
            if self.is_needed(text) >= 0:
                result_text.append(text)
        # print(result_text)
        for text in result_text:
            self.print(text)


a = []
text = ""
while True:
    b = input()
    if b.strip() == '' or b.strip() == '.':
        a.append(text)
        text = ""
    if b.strip() == 'Q' or b.strip() == 'q':
        a.append(text)
        text = ""
        break
    text += b + "\n"

foo = Foo("")
foo.extract_keyword(a)
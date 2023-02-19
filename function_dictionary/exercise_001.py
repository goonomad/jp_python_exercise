# 학생의 인적 사항 등록 후 검색 프로그램
# - 학번 , 이름 , 주소 

# { 학번 : { name : 이름 , addr : 주소 } }

# 1. 인적사항 등록
# 2. 검색 - 학번 검색
# 3. 수정
# 4. 삭제
# 5. 전체 보기
# 6. 종료

def dataInput(info):
    no = input("학번 입력 : ")
    name = input("이름 입력 : ")
    addr = input("주소 입력 : ")
    one = { no : { "name" : name , "addr" : addr }}
    if info.get(no) == None: 
        info.update(one)
        print("{}님이 추가되었습니다.".format(name))
    else:
        print("{}님이 이미 있습니다.".format(name))

def selectOne(info):
    no = input("검색할 학번 입력 : ")
    one = info.get(no)
    if one == None:
        print("학번이 잘못 입력되었습니다.")
    else:
        print("학번 : {}".format(no))
        print("이름 : {}".format(one['name']))
        print("주소 : {}".format(one['addr']))

def update(info):
    no = input("검색할 학번 입력 : ")
    one = info.get(no)
    if one == None:
        print("학번이 잘못되었습니다.")
    else:
        name = input("이름 입력 : ")
        addr = input("주소 입력 : ")
        one['name'] = name
        one['addr'] = addr

def delete(info):
    no = input("삭제할 학번 입력 : ")
    one = info.get(no)
    if one == None:
        print("학번이 잘못되었습니다.")
    else:
        name = input("삭제할 이름 입력 : ")
        if name == one['name']:
            print("{}님이 삭제되었습니다.".format(name))
            info.pop(no)
        else:
            print("이름이 잘못되었습니다.")    

def selectAll(info):
    print("학번\t이름\t주소")
    for no in info:
        one = info.get(no)
        print("{}\t{}\t{}".format(no,one['name'],one['addr']))

def esc():
    print("프로그램이 종료 됩니다.")
    exit(0)

def init(info):
    while True:
        select = int(input("1. 인적사항 등록\n2. 검색 - 학번 검색\n3. 수정\n4. 삭제\n5. 전체 보기\n6. 종료\n입력 : "))

        if select == 1:
            dataInput(info)
        elif select == 2:
            selectOne(info)
        elif select == 3:
            update(info)
        elif select == 4:
            delete(info)
        elif select == 5:
            selectAll(info)
        elif select == 6:
            esc()
        else:
            print("잘못된 메뉴 입력!!!")

info = {}
init(info)

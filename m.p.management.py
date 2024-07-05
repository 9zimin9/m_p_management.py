import hashlib

class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password_hash = self.hash_password(password)  # 비밀번호 해시 저장

    def hash_password(self, password):
        # 비밀번호 해시 함수 선택 (SHA-256 추천)
        hash_function = hashlib.sha256()

        # 해시값 생성
        password_utf8 = password.encode('utf-8')  # 문자열을 바이트열로 변환
        hash_function.update(password_utf8)
        hash_value = hash_function.hexdigest()  # 해시값 반환 까먹지 않기

        return hash_value

    def display(self):
        print(f"회원 이름: {self.name} ID: {self.username}")

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def display_title(self):
        print(self.title)

    def display_content(self):
        print(f"{self.title}\n{self.content}")

# ----- 코드 실행 ------
members = []

m1 = Member("Tim Burton", "T", "1111")
m2 = Member("Christopher Nolan", "C", "2222")
m3 = Member("박찬욱", "P", "3333")

members.append(m1)
members.append(m2)
members.append(m3)

print("초기 회원 목록")  # input으로 멤버 추가 기능 넣으면서 초기로 바뀜

for member in members:
    print(member.name)  # 이름만 출력

# 새로운 회원 추가(멤버 추가 기능 오래걸림, 다시 해봐야지)
def add_member():
    name = input("회원 이름을 입력하세요: ")
    username = input("회원 ID를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    new_member = Member(name, username, password)
    members.append(new_member)
    print(f"회원 {name}이(가) 추가되었습니다.")

posts = []

# post 인스턴스 9개
p1 = Post("이상한 나라의 앨리스 영화 아시죠?", "제가 만들었습니다.", "Tim Burton")
p2 = Post("거울 나라의 앨리스는 아세요?", "그것도 제가 만들었습니다.", "Tim Burton")
p3 = Post("하지만 저는 빅피쉬를 제일 좋아해요.", "꼭 보세요.", "Tim Burton")

p4 = Post("인셉션 다들 아시죠?", "제가 만들었습니다.", "Christopher Nolan")
p5 = Post("최근에 오펜하이머도 엄청났죠.", "그것도 제가 만들었습니다.", "Christopher Nolan")
p6 = Post("하지만 저는 메멘토를 제일 좋아해요.", "여러번 보세요, 전개가 어렵습니다.", "Christopher Nolan")

p7 = Post("저는 못생기면 죽는 병에 걸렸습니다.", "제가 만든 영화는 다 참 예뻐요.", "박찬욱")
p8 = Post("영화 아가씨 아시죠?", "제가 만들었습니다.", "박찬욱")
p9 = Post("하지만 저는 친절한 금자씨가 제일 좋더라구요.", "꼭 보세요, 헤어질 결심도,,", "박찬욱")

posts.append(p1)
posts.append(p2)
posts.append(p3)

posts.append(p4)
posts.append(p5)
posts.append(p6)

posts.append(p7)
posts.append(p8)
posts.append(p9)

# 새로운 게시물 추가(다시 봐야함,, 검색 너무 많이함)
def add_post():
    title = input("게시물 제목을 입력하세요: ")
    content = input("게시물 내용을 입력하세요: ")
    author = input("게시물 작성자 ID를 입력하세요: ")

    # 작성자 확인(어렵다.,,)
    author_name = None
    for member in members:
        if member.username == author:
            author_name = member.name
            break

    if author_name is None:
        print("작성자를 찾을 수 없습니다.")
    else:
        new_post = Post(title, content, author_name)
        posts.append(new_post)
        print(f"게시물 '{title}'이(가) 추가되었습니다.")

# 특정 작성자가 작성한 게시물 제목 출력
def display_posts_by_author(author):
    for post in posts:
        if post.author == author:
            post.display_title()

# 특정 단어가 포함된 게시물 제목 출력
def display_posts_by_keyword(keyword):
    for post in posts:
        if keyword in post.content:
            post.display_title()

# 메뉴 함수- 이걸 추가해야 화면에서 보이는듯,,?
def menu():
    while True:
        print("\n메뉴를 선택하세요:")
        print("1. 회원 추가")
        print("2. 게시물 추가")
        print("3. 특정 작성자의 게시물 보기")
        print("4. 특정 단어가 포함된 게시물 보기")
        print("5. 종료")
        choice = input("선택: ")

        if choice == '1':
            add_member()
        elif choice == '2':
            add_post()
        elif choice == '3':
            author = input("작성자 이름을 입력하세요: ")
            display_posts_by_author(author)
        elif choice == '4':
            keyword = input("검색할 단어를 입력하세요: ")
            display_posts_by_keyword(keyword)
        elif choice == '5':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

# 프로그램 시작
menu()


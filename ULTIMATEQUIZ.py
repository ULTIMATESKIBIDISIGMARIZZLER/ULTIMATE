import pgzrun

WIDTH=870
HEIGHT=650

marquee_box=Rect(0,0,880,80)
questions_box=Rect(0,0,650,150)
timer_box=Rect(0,0,150,150)

answer_box1=Rect(0,0,300,150)
answer_box2=Rect(0,0,300,150)
answer_box3=Rect(0,0,300,150)
answer_box4=Rect(0,0,300,150)

skip_box=(0,0,150,330)
score=0
time_left=30

question_file_name="ULTIMATEQUIZ/questions.txt"
marquee_message=""
is_game_over=False
answer_boxes=[answer_box1,answer_box2,answer_box3,answer_box4]

questions=[]
question_count=0
question_index=0

marquee_box.move_ip(0,0)
questions_box.move_ip(20,100)
timer_box.move_ip(700,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
skip_box.move_ip(700,270)

def draw():
    global marquee_message
    screen.clear()
    screen.fill(color="black")
    screen.draw.filled_rect(marquee_box,"black")
    screen.draw.filled_rect(questions_box,"navy blue")
    screen.draw.filled_rect(skip_box,"green")
    screen.draw.filled_rect(timer_box,"navy blue")

for answer_box in answer_boxes:
    screen.draw.filled_rect(answer_box,"dark orange")

marquee_message="Welcome to the ULTIMATE QUIZ......"

marquee_message=marquee_message+f"Q:{question_index} of {question_count}"

screen.draw.textbox(marquee_message, marquee_box, color="white")

screen.draw.textbox(
    str(time_left),timer_box,
    color="white", shadow=(0.5,0.5),
    scolor="dim grey"
)

screen.draw.textbox(
    "Skip",skip_box,
    color="black", angle=-90
)

screen.draw.textbox(
    question[0].strip(), questions_box,
    color="white", shadow=(0.5,0.5),
    scolor="dim grey"
)

index=1

for anwer_box in answer_boxes:
    screen.draw.textbox(question[index].strip(),answer_box, color="black")
    index=index+1





























































import turtle
import math
from time import strftime
from random import *

### Setting up Osiris' Window

wn = turtle.Screen()
osiris = turtle.Turtle()
wn.screensize(10000, 10000)
djet = strftime("%Y-%m-%d %H-%M-%S")

### SCREENSHOT COMMAND ON 'A' KEYBOARD PRESS ###

def ihy():
    ts = osiris.getscreen()
    osiris.hideturtle()
    ts.getcanvas().postscript(file="horus - " + djet +
                              ".eps", width=5000, height=5000)
    osiris.showturtle()
    print ('screenshot taken')
turtle.onkey(ihy,"a")
turtle.listen()

### CENTRE DOT COMMAND ON 'D' KEYBOARD PRESS ###

def yam():
    osiris.penup()
    osiris.goto(0,0)
    osiris.dot(3,'#0000FF')
    
turtle.onkey(yam,"d")
turtle.listen()

### MATH DEFINITIONS ###

def pythag(sidea, sideb):
    csquare = (sidea ** 2) + (sideb ** 2)
    sidec = math.sqrt(csquare)
    return sidec

def eq_triangle_height(side):
    eqheight = (math.sqrt(3)/2)* side
    return eqheight

def work_sin(sin_length,sin_angle):
    sin_number = ((math.sin(math.radians(sin_angle)))*sin_length)
    return sin_number

    ## Example 1: https://www.mathsisfun.com/algebra/trig-solving-sas-triangles.html##

def work_cos_sas(side_1,side_2,cos_angle):
    cos_b = (side_1 ** 2) 
    cos_c = (side_2 ** 2)
    cos_1 = (math.cos(math.radians(cos_angle)))
    cos_workout_1 = (cos_b + cos_c) - (2 * side_1 * side_2 * cos_1)
    cos_number = math.sqrt(cos_workout_1)
    return cos_number

def work_sin_by_sin(sin_length_1,sin_angle_1,sin_length_2,sin_angle_2):
    sin_1 = (sin_length_1/(math.sin(math.radians(sin_angle_1))))
    sin_2 = (math.sin(math.radians(sin_angle_2))* sin_length_2)
    sin_number = sin_1 * sin_2
    return sin_number

def work_cos(cos_length,cos_angle):
    cos_number = ((math.cos(math.radians(cos_angle)))*cos_length)
    return cos_number

def work_tan(work_tan_a,work_tan_b):
    work_tan_angle = (work_tan_a / work_tan_b)
    work_tan_number = (math.degrees(math.atan(work_tan_angle)))
    return work_tan_number  
    
def work_tan_opp(tan_opp_length,tan_opp_angle):
    tan_opp_number = ((math.tan(math.radians(tan_opp_angle)))*tan_opp_length)
    return tan_opp_number        

def work_sin_opp(sin_opp_angle_adj,sin_opp_angle_opp,sin_opp_length):
    sin_opp_a = (math.sin(math.radians(sin_opp_angle_adj)))
    sin_opp_b = sin_opp_length / sin_opp_a
    sin_opp_c = sin_opp_b * (math.sin(math.radians(sin_opp_angle_opp)))
    return sin_opp_c  

def work_acos(A,B,C):
    X = math.degrees(math.acos(((C ** 2) + (A ** 2) - (B ** 2))/(2.0 * C * A))) 
    return X


################## GEOMETRIC DEFINITIONS ####################
##################        START          ####################



def aker(aker_y=1,aker_span=10,aker_start=-50,
         aker_start_increase = 15,aker_no=5,aker_length=300,
         aker_length_increase=-30,aker_angle=12,aker_angle_increase=5,
         aker_gap=10,aker_gap_increase=2,aker_pensize=3,aker_color='#F09900'):
    if aker_y == 1:
        osiris.penup()
        osiris.pencolor(aker_color)
        osiris.pensize(aker_pensize)
        osiris.setheading(osirisHeadingStart)
        osiris.forward(aker_start)
        osirisCurrentX = osiris.xcor()
        osirisCurrentY = osiris.ycor()
        for aker_d in range(1,3):
            osiris.setheading(osirisHeadingStart)
            if aker_d == 1:
                osiris.right(90)
            else:
                osiris.left(90)
            osiris.forward(aker_span)
            osiris.dot(2)
            osirisTemporaryX = osiris.xcor()
            osirisTemporaryY = osiris.ycor()
            for aker_e in range(1,(aker_no+1)):
                osiris.setheading(osirisHeadingStart)
                if aker_d == 1:
                    osiris.right(aker_angle+(aker_e*aker_angle_increase))
                else:
                    osiris.left(aker_angle+(aker_e*aker_angle_increase))
                osiris.pendown()
                osiris.forward(aker_length+(aker_e*aker_length_increase))
                osiris.penup()
                osiris.goto(osirisTemporaryX,osirisTemporaryY)                    
                osiris.setheading(osirisHeadingStart)
                osiris.forward(aker_e*aker_start_increase)
                if aker_d == 1:
                    osiris.right(90)
                else:
                    osiris.left(90)
                osiris.forward(aker_gap*(aker_e*aker_gap_increase))
            osiris.goto(osirisCurrentX,osirisCurrentY)
        osiris.setheading(osirisHeadingStart)


  

def amun(amun_y,amun_no,amun_angle_a,amun_angle_b,
         amun_forward_a,amun_forward_b,
         amun_pensize,amun_color):
    if amun_y == 1:
        for amun_a in range(amun_no):
            osiris.penup()
            osiris.pencolor(amun_color)
            osiris.pensize(amun_pensize)
            osiris.goto(0,0)				
            osiris.right(randint(amun_angle_a,amun_angle_b))
            osiris.pendown()
            osiris.forward(randint(amun_forward_a,amun_forward_b))
        osiris.penup()

def amunet(amunet_y,amunet_start,amunet_size,
           amunet_pensize,amunet_color):
    if amunet_y == 1:
        osiris.forward(amunet_start)
        osiris.pensize(amunet_pensize)
        osiris.color(amunet_color)
        osiris.pendown()
        osiris.right(45)
        osiris.forward(amunet_size)
        for b in range(1,4):
            osiris.left(90)
            osiris.forward(amunet_size)
            if b == 1:
                osirisCurrentX = osiris.xcor()  
                osirisCurrentY = osiris.ycor()
        osiris.penup()
        osiris.goto(osirisCurrentX, osirisCurrentY)    
        osiris.setheading(osirisHeadingStart)


def anhur(anhur_y,anhur_start,anhur_no,
          anhur_size,anhur_spacing,
          anhur_pensize,anhur_color):
    if anhur_y == 1:
        osiris.pensize(anhur_pensize)
        osiris.color(anhur_color)
        osirisTemporaryX = osiris.xcor() 
        osirisTemporaryY = osiris.ycor()
        for anhur_c in range(anhur_no):
            osiris.penup()
            osiris.goto(osirisTemporaryX, osirisTemporaryY)   
            osiris.setheading(osirisHeadingStart)
            osiris.forward((anhur_start) + (anhur_spacing * anhur_c))
            # This is marked here as it will mark the top chevron
            osirisCurrentX = osiris.xcor() 
            osirisCurrentY = osiris.ycor() 
            osiris.right(135)
            osiris.pendown()
            osiris.pensize(2)
            anhur_calsize = ((anhur_size) -
                             ((anhur_size/anhur_no) * anhur_c))
            osiris.forward(anhur_calsize)
            osiris.backward(anhur_calsize)
            osiris.right(90)
            osiris.forward(anhur_calsize)
        osiris.penup()
        osiris.goto(osirisCurrentX, osirisCurrentY)    
        osiris.setheading(osirisHeadingStart)


def anput(anput_y,anput_start,anput_outer,
          anput_outer_size,anput_outerpensize,
          anput_innerpensize,anput_color,):
    if anput_y == 1:
        osiris.penup()
        osiris.pensize(anput_outerpensize)
        osiris.color(anput_color)
        osiris.setheading(osirisHeadingStart)
        osiris.forward(anput_start)
        osirisCurrentX = osiris.xcor()
        osirisCurrentY = osiris.ycor()
        if anput_outer == 1:
            for anput_a in range(1,3):
                osiris.goto(osirisCurrentX,osirisCurrentY)
                osiris.setheading(osirisHeadingStart)
                osiris.pendown()
                if anput_a == 1:
                    osiris.right(60)
                else:
                    osiris.left(60)
                osiris.forward(anput_outer_size)
                if anput_a == 1:
                    osiris.left(60)
                else:
                    osiris.right(60)
                osiris.forward(anput_outer_size)
                if anput_a == 1:
                    osiris.left(60)
                else:
                    osiris.right(60)
                osiris.forward(anput_outer_size/3)
                if anput_a == 1:
                    osiris.right(120)
                else:
                    osiris.left(120)
                osiris.forward(anput_outer_size/3)
                for anput_b in range(1,3):
                    if anput_a == 1:
                        osiris.left(60)
                    else:
                        osiris.right(60)
                    osiris.forward(anput_outer_size)
                osiris.penup()
        osiris.goto(osirisCurrentX,osirisCurrentY)
        osiris.setheading(osirisHeadingStart)
        osiris.penup()
        # Now we need to move to the centre of the helix
        osiris.right(60)
        osiris.pensize(anput_innerpensize)
        osiris.forward(anput_outer_size)
        osiris.left(120)
        osiris.forward(anput_outer_size)
        def anput_inner():
            for anput_c in range(1,4):         
                osiris.forward(anput_outer_size/1.5)
                osiris.right(120)
                for anput_d in range(1,4):
                        osiris.forward(anput_outer_size/3)
                        osiris.right(120)
            osiris.left(60)
        for anput_e in range(1,3):
            for anput_f in range(1,7):
                osiris.pendown()
                anput_inner()
                osiris.penup()
            if anput_e == 1:
                osiris.left(120)
                osiris.backward(anput_outer_size/0.75)
        osiris.setheading(osirisHeadingStart)
        osiris.forward(anput_outer_size*1)
        osirisCurrentX = osiris.xcor() 
        osirisCurrentY = osiris.ycor()

def anubis(anubis_y,anubis_no,anubis_size,anubis_reduction,
           anubis_dot_y,anubis_dot_no,anubis_dot_size,
           anubis_crosses_y,anubis_cross_no,anubis_cross_size,
           anubis_cross_reduction,anubis_pensize,anubis_color):
    if anubis_y == 1:
        anubis_xy = anubis_size / 2
        osiris.penup()
        osiris.color(anubis_color)
        osiris.pensize(anubis_pensize)
        osiris.goto(anubis_xy,anubis_xy)
        osiris.setheading(90)
        for anubis_c in range (1,(anubis_no+1)):
            for anubis_d in range (1,5):
                osiris.pendown()
                osiris.left(90)
                osiris.forward(anubis_size)
            osiris.penup() 
            # Decide if we want to draw crosses
            if anubis_crosses_y == 1:
                anubis_size = anubis_size - anubis_reduction
                anubis_xy = anubis_xy - (anubis_reduction/2)
                osiris.goto(anubis_xy,anubis_xy)
                osiris.setheading(90)
                anubis_cross_space = anubis_size / anubis_cross_no
                for anubis_d in range (1,5):
                    osiris.left(90)
                    for anubis_e in range(anubis_cross_no):
                        osirisReturnX = osiris.xcor()
                        osirisReturnY = osiris.ycor()
                        for anubis_f in range(1,5):
                            osiris.left(90)
                            osiris.pendown()
                            osiris.forward(anubis_cross_size/2)
                            osiris.penup()
                            osiris.goto(osirisReturnX, osirisReturnY)
                        osiris.forward(anubis_cross_space)          
            # End of cross logic
            # Decide if we want to draw dots
            if anubis_dot_y == 1:
                anubis_size = anubis_size - anubis_reduction
                anubis_xy = anubis_xy - (anubis_reduction/2)
                osiris.goto(anubis_xy,anubis_xy)
                osiris.setheading(90)
                anubis_dot_space = anubis_size / anubis_dot_no
                for anubis_d in range (1,5):             
                    osiris.left(90)
                    for anubis_e in range(anubis_dot_no):
                        osiris.pendown()
                        osiris.dot(anubis_dot_size)
                        osiris.penup()
                        osiris.forward(anubis_dot_space)
            # End of dot logic
            anubis_size = anubis_size - anubis_reduction
            anubis_xy = anubis_xy - (anubis_reduction/2)
            osiris.goto(anubis_xy,anubis_xy)
            osiris.setheading(90)
            anubis_cross_no = anubis_cross_no - anubis_cross_reduction
        # If we want to draw dots or crosses then
        # We don't need the final square
        if anubis_dot_y == 1 or anubis_crosses_y == 1:
            for anubis_k in range (1,5):
                osiris.pendown()
                osiris.left(90)
                osiris.forward(anubis_size)
            osiris.penup()


def apedemak(
    apedemak_y=1,apedemak_start=0,
    apedemak_span_angle=70,apedemak_spike_inner_angle= 60,
    apedemak_length = 400,apedemak_spike_no = 5,
    apedemak_little_spike = 1,apedemak_little_spike_type = 'percentage',
    apedemak_little_spike_reduction = 0.5,adepemak_slash_space = 0.5,
    adepemak_slash_extension = 200,adepemak_slash_no = 3,
    apedemak_spike_pensize = 4,apedemak_spike_color = '#FF4400',
    apedemak_little_spike_pensize = 3,apedemak_little_spike_color = '#FF4499',
    apedemak_slash_pensize = 6,apedemak_slash_color = '#4444FF'        
    ):
    if apedemak_y == 1:
        ### Universal Settings
        osiris.setheading(osirisHeadingStart)
        osiris.forward(apedemak_start)
        osirisReturnX = osiris.xcor()
        osirisReturnY = osiris.ycor()
        apedemak_bottom_angle = (apedemak_span_angle/2)
        apedemak_outer_line = apedemak_length + adepemak_slash_extension

        ### Upward Spike Measurements
        apedemak_spike_angle = (180 - 90 
                               - apedemak_spike_inner_angle) # Angle from centre

        ### Downward Slash Measurements
        # Used for calculating top splash
        apedemak_slash_angle_a = (180 - apedemak_spike_angle -
                                  apedemak_bottom_angle)

        # Height from the bottom of the cone to the top of the middle    
        apedemak_height = (work_sin_opp(apedemak_spike_inner_angle,
                                        apedemak_slash_angle_a,
                                        apedemak_length))

        # The top slash line - also used to calculate the other slashes
        apedemak_slash_first_line = (work_cos_sas(apedemak_outer_line,
                                                apedemak_height,
                                                apedemak_bottom_angle))
        
        # The top most outer angle    
        apedemak_slash_top_angle = (work_acos(apedemak_outer_line,
                                        apedemak_height,
                                        apedemak_slash_first_line))
        
        # The maximum height between the bottom and top slash terminal points
        apedemak_slash_terminal_height = (apedemak_height *
                                          adepemak_slash_space)

        # The gap between where the downward slash lines terminate    
        apedemak_slash_gap = (apedemak_slash_terminal_height /
                              (adepemak_slash_no - 1))

        # The angle for the top slash from the top-middle of the cone
        apedemak_slash_angle_b = (180 - apedemak_bottom_angle
                                  - apedemak_slash_top_angle)
        for apedemak_a in range(1,3):
            osiris.setheading(osirisHeadingStart)
            osiris.goto(osirisReturnX, osirisReturnY)
            apedemak_spike_outer_length = apedemak_length
            # Calculation to reduce the distance that Osiris
            # starts each spike at.
            apedemak_red_distance = (apedemak_length
                                     / apedemak_spike_no)
            for apedemak_g in range(1,apedemak_spike_no+1):
                osiris.goto(osirisReturnX, osirisReturnY)                
                # The distance from where the spike starts
                # to the centre of the cone - at a 90 degree angle.
                # We can't use secant so need this workaround :(
                apedemak_spike_hor = (work_sin
                                      (apedemak_spike_outer_length,
                                       apedemak_bottom_angle))
                # The distance from the above calculation terminates
                # at the centre of the cone to where the spike will
                # terminate at - we already know the angle we want to use
                apedemak_spike_upwards = (work_tan_opp
                                          (apedemak_spike_hor,
                                           apedemak_spike_angle))
                
                apedemak_spike_length = pythag(apedemak_spike_upwards,
                                              apedemak_spike_hor)
                # We need this measurement to work out the first slash
                # later in the function
                if apedemak_g == 1:
                    apedemak_slash_measure_a = apedemak_spike_length

                ### Now we can begin to move Osiris around 
                osiris.setheading(osirisHeadingStart)
                if apedemak_a == 1:
                    osiris.left(apedemak_bottom_angle)
                else:
                    osiris.right(apedemak_bottom_angle)
                osiris.forward(apedemak_spike_outer_length)
                osiris.setheading(osirisHeadingStart)
                if apedemak_a == 1:                
                    osiris.right(90-apedemak_spike_angle)
                else:                
                    osiris.left(90-apedemak_spike_angle)
                osiris.pendown()
                osiris.pensize(apedemak_spike_pensize)
                osiris.color(apedemak_spike_color)
                osiris.forward(apedemak_spike_length)
                osiris.penup()
                osiris.goto(osirisReturnX, osirisReturnY)
                # Make sure the little spikes start half the distance
                # of the big spikes
                apedemak_little_spike_start = (apedemak_spike_outer_length
                                                 -(apedemak_red_distance/2))
                # Little Spike Measurements - Use the same logic as
                # the build up for the big spikes above in the function
                apedemak_little_spike_hor = (work_sin(apedemak_little_spike_start,
                                              apedemak_bottom_angle))
                apedemak_little_spike_height = (work_tan_opp(apedemak_little_spike_hor,
                                                   apedemak_spike_angle))
                apedemak_little_spike_length = pythag(apedemak_little_spike_height,
                                              apedemak_little_spike_hor)                
                if apedemak_little_spike == 1:
                    if apedemak_little_spike_type == 'percentage':
                        # Working out where the little line gap
                        apedemak_little_spike_gap = (apedemak_little_spike_length * 
                                                apedemak_little_spike_reduction)

                        # work out the little line actual length
                        apedemak_little_spike_actual_length = (apedemak_little_spike_length -
                                                              apedemak_little_spike_gap)

                    if apedemak_little_spike_type == 'consistent':
                        # Working out where the little line gap
                        apedemak_little_spike_gap = (apedemak_little_spike_length -
                                                     apedemak_little_spike_reduction)

                        # work out the little line actual length
                        apedemak_little_spike_actual_length = (apedemak_little_spike_length -
                                                               apedemak_little_spike_gap)
                    osiris.setheading(osirisHeadingStart)
                    if apedemak_a == 1:
                        osiris.left(apedemak_bottom_angle)
                    else:
                        osiris.right(apedemak_bottom_angle)
                    osiris.forward(apedemak_little_spike_start)
                    # Get osiris into position for the actual drawn line)
                    osiris.setheading(osirisHeadingStart)
                    if apedemak_a == 1:                
                        osiris.right(90-apedemak_spike_angle)
                    else:                
                        osiris.left(90-apedemak_spike_angle)
                    osiris.forward(apedemak_little_spike_gap)
                    osiris.pendown()
                    osiris.pensize(apedemak_little_spike_pensize)
                    osiris.color(apedemak_little_spike_color)
                    osiris.forward(apedemak_little_spike_actual_length)
                    osiris.penup()        
                # The actual length of the outside line
                apedemak_spike_outer_length = (apedemak_spike_outer_length-
                                               apedemak_red_distance)
            ### Start of the slashes
            osiris.goto(osirisReturnX, osirisReturnY)
            osiris.setheading(osirisHeadingStart)
            if apedemak_a == 1:
                osiris.left(apedemak_bottom_angle)
            else:
                osiris.right(apedemak_bottom_angle)
            osiris.forward(apedemak_outer_line)
            if apedemak_a == 1:
                osiris.right(180-apedemak_slash_top_angle)
            else:
                osiris.left(180-apedemak_slash_top_angle)        
            osiris.pendown()
            osiris.pensize(apedemak_slash_pensize)
            osiris.color(apedemak_slash_color)
            osiris.forward(apedemak_slash_first_line)
            osiris.penup()
            for apedemak_t in range(1,adepemak_slash_no):
                # The slash gap has to increase on each iteration
                apedemak_slash_gap_dymanic = (apedemak_slash_gap *
                                              apedemak_t)
                # The length of the slash - for the second line onwards 
                apedemak_slash_length_2plus = work_cos_sas(apedemak_slash_first_line,
                                                  apedemak_slash_gap_dymanic,
                                                  apedemak_slash_angle_b)
                # The top outer angle - for the second line onwards 
                apedemak_slash_angle_2plus = work_acos(apedemak_slash_first_line,
                                                   apedemak_slash_gap_dymanic,
                                                   apedemak_slash_length_2plus)
                osiris.goto(osirisReturnX, osirisReturnY)
                osiris.setheading(osirisHeadingStart)
                if apedemak_a == 1:
                    osiris.left(apedemak_bottom_angle)
                else:
                    osiris.right(apedemak_bottom_angle)
                osiris.forward(apedemak_outer_line)
                if apedemak_a == 1:
                    osiris.right(180-apedemak_slash_top_angle+apedemak_slash_angle_2plus)
                else:
                    osiris.left(180-apedemak_slash_top_angle+apedemak_slash_angle_2plus)        
                osiris.pendown()
                osiris.forward(apedemak_slash_length_2plus)
                osiris.penup()    
        

def apep(apep_y,apep_size,apep_square_y_n,
         apep_stroke,apep_no,apep_quads,
         apep_pen_size,apep_fill_color,apep_pen_color):
    ## THIS IS THE SHAPE WITHIN THE TILE ##
    def apep_square():
        osiris.pensize(apep_pen_size)
        osiris.pencolor(apep_pen_color)
        osiris.fillcolor(apep_fill_color)
        osiris.penup()
        osiris.setheading(90)
        osirisCurrentX= osiris.xcor()
        osirisCurrentY= osiris.ycor()
        ## DRAWS OUTER SQUARE IF 1 IN INTEGAR##
        if apep_square_y_n == 1:
            osiris.goto((osirisCurrentX-(apep_size/2)),
                        (osirisCurrentY+(apep_size/2)))
            for apep_b in range(1,5):
                osiris.right(90)
                osiris.pendown()
                osiris.forward(apep_size)
        ## GET INTO POSITION FOR THE QUADS
        apep_short = ((apep_size / apep_quads)/2)
        apep_long = pythag(apep_short,apep_short)
        osiris.goto((osirisCurrentX-(apep_size/2)),
                    (osirisCurrentY+(apep_size/2)))
        osiris.setheading(90)
        osiris.right(135)
        ## MOVE TO THE CENTRE OF THE QUAD
        osiris.forward(apep_long)        
        for apep_p in range(apep_quads):
            osirisxret = osiris.xcor()
            osirisyret = osiris.ycor()
            for apep_q in range(apep_quads):
                osirisTemporaryX = osiris.xcor()
                osirisTemporaryY = osiris.ycor()
                osiris_quad_heading = 90
                ## draw the top left triangles
                for apep_r in range(1,5):
                    osiris.setheading(osiris_quad_heading)
                    apep_fill = randint(1,2)
                    if apep_stroke == 1:
                        osiris.pendow()
                    if apep_fill == 1:
                        osiris.begin_fill()
                    for apep_t in range (1,5):
                        osiris.forward(apep_short)
                        osiris.left(90)                        
                    if apep_fill == 1:
                        osiris.end_fill()
                    osiris.penup()
                    osiris_quad_heading = osiris_quad_heading + 90
                osiris.goto(osirisTemporaryX,osirisTemporaryY)
                osiris.setheading(270)
                osiris.forward(apep_short *2)
            osiris.goto(osirisxret,osirisyret)
            osiris.setheading(0)
            osiris.forward(apep_short *2)
        osiris.setheading(90)
        osiris.goto(osirisCurrentX,osirisCurrentY)
    ############ THIS IS THE TILE EXECUTION ##########################
    ### DRAW A CENTRAL TILE ###
    if apep_y == 1:
        osiris.goto(0,0)
        apep_square()
        ### MOVING UP AND DRAW OTHER TILES LIKE A SNAKE ###
        for apep_a in range(1,(apep_no+1)): # HOW MANY OUTER RINGS?
                for apep_b in range(1,(2+((apep_a-1)*2))): # TOP ROW
                    if apep_b > 1:
                        osiris.right(90)
                    osiris.forward(apep_size)
                    apep_square()
                for apep_c in range(1,(3+((apep_a-1)*2))): # RIGHT COLUMN
                    if apep_c > 1:
                        osiris.right(180)
                    else:
                        osiris.right(90)
                    osiris.forward(apep_size)
                    apep_square()
                for apep_d in range(1,(3+((apep_a-1)*2))): # BOTTOM ROW
                    if apep_d > 1:
                        osiris.right(270)
                    else:
                        osiris.right(180)
                    osiris.forward(apep_size)
                    apep_square()
                for apep_e in range(1,(4+((apep_a-1)*2))): #LEFT COLUMN
                    if apep_e > 1:
                        osiris.right(0)
                    else:
                        osiris.right(270)
                    osiris.forward(apep_size)
                    apep_square()
   

def aten(aten_y,aten_start,aten_circle_size,aten_gap,
         aten_ray_no,aten_ray_span,aten_ray_length,
         aten_pensize,aten_ray_pensize,aten_color):
    if aten_y == 1:
        osiris.penup()
        osiris.setheading(osirisHeadingStart)
        osiris.forward(aten_start)
        osiris.pensize(aten_pensize)
        osiris.pencolor(aten_color)
        osiris.right(90) # Need to get in position for the circle start
        osiris.pendown()
        osiris.circle(aten_circle_size,360)
        osiris.penup()
        osiris.setheading(osirisHeadingStart)
        osiris.forward(aten_circle_size) # Move to the circle middle
        osirisCurrentX = osiris.xcor()
        osirisCurrentY = osiris.ycor()
        aten_angle_increase = (aten_ray_span/(aten_ray_no-1))
        for aten_a in range(1,3):
            for aten_b in range(1,(aten_ray_no+1)):
                osiris.goto(osirisCurrentX, osirisCurrentY)
                osiris.setheading(osirisHeadingStart)
                if aten_a == 1:
                    osiris.right(90)
                else:
                    osiris.left(90)
                osiris.forward(aten_gap)
                osiris.setheading(osirisHeadingStart)
                # We have to go the opposite way here to normal logic
                # to give us the correct angle or it's out of position
                if aten_a == 1:
                    osiris.left(270 + ((aten_ray_span/2) -
                                       (aten_angle_increase *
                                        (aten_b-1))))
                else:
                    osiris.right(270 + ((aten_ray_span/2) -
                                       (aten_angle_increase *
                                        (aten_b-1)))) 
                osiris.pendown()
                osiris.pensize(aten_ray_pensize)
                osiris.forward(aten_ray_length)
                osiris.penup()
        osiris.goto(osirisCurrentX, osirisCurrentY)
        osiris.setheading(osirisHeadingStart)
        osiris.forward(aten_circle_size)

                 

def bast(bast_y,bast_start,bast_angle,
         bast_forward,bast_no,bast_pensize,
         bast_color,osirisStartingX,osirisStartingY):
    if bast_y == 1:
        osiris.penup()
        osiris.pensize(bast_pensize)
        osiris.color(bast_color)
        osiris.goto(osirisStartingX,osirisStartingY)
        osiris.setheading(osirisHeadingStart)
        osiris.forward(bast_start)
        osirisTemporaryX = osiris.xcor() 
        osirisTemporaryY = osiris.ycor()
        for bast_a in range(1,3):
            osiris.goto(osirisTemporaryX,osirisTemporaryY)
            osiris.setheading(osirisHeadingStart)
            osiris.pendown()
            if bast_a == 1:
                osiris.right(bast_angle)
            else:
                osiris.left(bast_angle)
            osiris.forward(bast_forward)
            if bast_a == 1:
                osiris.left(bast_angle*3)
            else:
                osiris.right(bast_angle*3)
            osiris.forward(bast_forward*1.5)
            if bast_a == 1:
                osiris.right(bast_angle)
            else:
                osiris.left(bast_angle)
            osiris.forward(bast_forward*2)
            # END OF NORMAL BAST ZIG ZAG
            # NOW WE WANT TO PUT IN SOME IF CONDITIONS
            if bast_no >= 2: 
                if bast_a == 1:
                    osiris.right(bast_angle*3)
                else:
                    osiris.left(bast_angle*3)
                osiris.forward(bast_forward*3)
                if bast_a == 1:
                    osiris.left(bast_angle)
                else:
                    osiris.right(bast_angle)
                osiris.forward(bast_forward*2)
            if bast_no >= 3: 
                if bast_a == 1:
                    osiris.left(bast_angle*2.5)
                else:
                    osiris.right(bast_angle*2.5)
                osiris.forward(bast_forward*3.5)
                if bast_a == 1:
                    osiris.right(bast_angle)
                else:
                    osiris.left(bast_angle)
                osiris.forward(bast_forward*4) 
            osiris.penup()
        

def bennu(bennu_y,bennu_size,bennu_square_y_n,
          bennu_stroke,bennu_no,bennu_quads,
          bennu_pen_size,bennu_fill_color,bennu_pen_color):
    osiris.goto(0,0)
    ## THIS IS THE SHAPE WITHIN THE TILE ##
    def bennu_square():
        osiris.pensize(bennu_pen_size)
        osiris.pencolor(bennu_pen_color)
        osiris.fillcolor(bennu_fill_color)
        osiris.penup()
        osiris.setheading(90)
        osirisCurrentX = osiris.xcor()
        osirisCurrentY = osiris.ycor()
        ## DRAWS OUTER SQUARE IF 1 IN INTEGAR##
        if bennu_square_y_n == 1:
            osiris.goto((osirisCurrentX-(bennu_size/2)),
                        (osirisCurrentY+(bennu_size/2)))
            for bennu_b in range(1,5):
                osiris.right(90)
                osiris.pendown()
                osiris.forward(bennu_size)
        ## GET INTO POSITION FOR THE INNER TRIANGLES
        osiris.penup()
        bennu_short = ((bennu_size / bennu_quads)/2)
        bennu_long = pythag(bennu_short,bennu_short)
        osiris.goto ((osirisCurrentX-(bennu_size/2))
                     ,(osirisCurrentY+(bennu_size/2)))
        osiris.setheading(90)
        osiris.right(135)
        ## MOVE TO THE CENTRE OF THE QUAD
        osiris.forward(bennu_long)        
        for bennu_p in range(bennu_quads):
            osirisxret = osiris.xcor()
            osirisyret = osiris.ycor()
            for bennu_q in range(bennu_quads):
                osirisTemporaryX = osiris.xcor()
                osirisTemporaryY = osiris.ycor()
                osiris_quad_heading = 90
                ## draw the top left triangles
                for bennu_r in range(1,5):
                    osiris.setheading(osiris_quad_heading)
                    for bennu_s in range (1,3):
                        bennu_fill = randint(1,2)
                        if bennu_stroke == 1:
                            osiris.pendown()
                        if bennu_fill == 1:
                            osiris.begin_fill()
                        osiris.forward(bennu_short)
                        osiris.left(135)
                        osiris.forward(bennu_long)
                        osiris.left(135)
                        osiris.forward(bennu_short)
                        if bennu_fill == 1:
                            osiris.end_fill()
                        osiris.penup()
                        ## get in position for the second triangle
                        osiris.left(135)
                        osiris.forward(bennu_long)
                        osiris.left(135)
                    osiris_quad_heading = osiris_quad_heading + 90
                osiris.goto(osirisTemporaryX,osirisTemporaryY)
                osiris.setheading(270)
                osiris.forward(bennu_short *2)
            osiris.goto(osirisxret,osirisyret)
            osiris.setheading(0)
            osiris.forward(bennu_short *2)
        osiris.setheading(90)
        osiris.goto(osirisCurrentX,osirisCurrentY)
    ############ THIS IS THE TILE EXECUTION ##########################
    ### DRAW A CENTRAL TILE ###
    if bennu_y == 1:
        bennu_square()
        ### MOVING UP AND DRAW OTHER TILES LIKE A SNAKE ###
        for bennu_a in range(1,(bennu_no+1)): #HOW MANY OUTER RINGS?
                for bennu_b in range(1,(2+((bennu_a-1)*2))): #TOP ROW
                    if bennu_b > 1:
                        osiris.right(90)
                    osiris.forward(bennu_size)
                    bennu_square()
                for bennu_c in range(1,(3+((bennu_a-1)*2))): #RIGHT COLUMN
                    if bennu_c > 1:
                        osiris.right(180)
                    else:
                        osiris.right(90)
                    osiris.forward(bennu_size)
                    bennu_square()
                for bennu_d in range(1,(3+((bennu_a-1)*2))): #BOTTOM ROW
                    if bennu_d > 1:
                        osiris.right(270)
                    else:
                        osiris.right(180)
                    osiris.forward(bennu_size)
                    bennu_square()
                for bennu_e in range(1,(4+((bennu_a-1)*2))): #LEFT COLUMN
                    if bennu_e > 1:
                        osiris.right(0)
                    else:
                        osiris.right(270)
                    osiris.forward(bennu_size)
                    bennu_square()

                    
def geb(geb_y=1,geb_no=1,geb_circum_a=20,geb_circum_b=200,
        geb_distance_a=100,geb_distance_b=300,
        geb_circle_reduction_a=5,geb_circle_reduction_b=30,
        geb_pensize=1,geb_pencolor='#FF0000',geb_fillcolor='#FF0000'):
    if geb_y == 1:
        for geb_a in range(1,(geb_no+1)):
            osiris.pencolor(geb_pencolor)
            osiris.pensize(geb_pensize)
            osiris.fillcolor(geb_fillcolor)
            osiris.setheading(90)
            osiris.goto(0,0)
            osiris.right(randint(0,360))
            geb_circum_one=(randint(geb_circum_a,geb_circum_b))
            geb_distance_one=randint(geb_distance_a,geb_distance_b)
            geb_distance_two=(randint(geb_circle_reduction_a,
                                      geb_circle_reduction_b))
            geb_distance_three=geb_distance_one + geb_distance_two
            osiris.forward(geb_distance_one)
            osiris.pendown()
            osiris.begin_fill()
            osiris.forward(geb_distance_two)
            osiris.left(90)
            osiris.circle(geb_distance_three,geb_circum_one)
            osiris.left(90)
            osiris.forward(geb_distance_two)
            osiris.left(90)
            osiris.circle(-geb_distance_one,geb_circum_one)
            osiris.end_fill()
            osiris.penup()
            
            
def hapi(hapi_y=1,hapi_start=0,hapi_length=300,
         hapi_angle=30,hapi_line_no=10,hapi_section_no=3,
         hapi_space=20,hapi_pensize=5,hapi_color='#FF3333'):    
    if hapi_y == 1:
        osiris.penup()
        osiris.pensize(hapi_pensize)
        osiris.color(hapi_color)
        osiris.setheading(osirisHeadingStart)
        osiris.forward(hapi_start)
        osirisCurrentX = osiris.xcor()
        osirisCurrentY = osiris.ycor()
        for hapi_a in range(1,hapi_section_no+1):
            osiris.goto(osirisCurrentX,osirisCurrentY)
            osirisReturnX = osiris.xcor()
            osirisReturnY = osiris.ycor()
            osiris.setheading(osirisHeadingStart)           
            for hapi_b in range(1,3):
                if hapi_b == 1:
                    osiris.right(90)
                else:
                    osiris.left(90)
                hapi_outer_line_position = ((hapi_space
                                             * (hapi_line_no-1))/2)
                osiris.forward(hapi_outer_line_position)
                osirisTemporaryX = osiris.xcor()
                osirisTemporaryY = osiris.ycor()
                for hapi_c in range(1,(hapi_line_no+1)):
                    osiris.setheading(osirisHeadingStart)
                    if hapi_b == 1:
                        osiris.left(hapi_angle)
                    else:
                        osiris.right(hapi_angle)
                    osiris.pendown()
                    osiris.forward(hapi_length)
                    osiris.setheading(osirisHeadingStart)
                    if hapi_b == 1:
                        osiris.right(hapi_angle)
                    else:
                        osiris.left(hapi_angle)
                    osiris.forward(hapi_length)
                    osiris.penup()
                    if hapi_b == 1 and hapi_c == 1:
                        osiris.setheading(osirisHeadingStart)
                        osiris.left(90)
                        osiris.forward(hapi_outer_line_position)
                        osirisCurrentX = osiris.xcor()
                        osirisCurrentY = osiris.ycor() 
                    osiris.goto(osirisTemporaryX,osirisTemporaryY)    
                    osiris.setheading(osirisHeadingStart)
                    if hapi_b == 1:
                        osiris.left(90)
                    else:
                        osiris.right(90)
                    osiris.forward(hapi_space)
                    osirisTemporaryX = osiris.xcor()
                    osirisTemporaryY = osiris.ycor()
                    osiris.setheading(osirisHeadingStart)
                osiris.goto(osirisReturnX,osirisReturnY)
                osiris.setheading(osirisHeadingStart)
            osiris.goto(osirisCurrentX,osirisCurrentY)

     
   
def hathor(hathor_y,hathor_start,hathor_span,
           hathor_no,hathor_gap,hathor_angle,
           hathor_length,hathor_reduction,
           hathor_indent,hathor_spacing,
           hathor_pensize,hathor_color):
    if hathor_y == 1:
        osiris.forward(hathor_start)
        osiris.pensize(hathor_pensize)
        osiris.color(hathor_color)
        osirisCurrentX = osiris.xcor() 
        osirisCurrentY = osiris.ycor()
        for hathor_a in range(1,3):
            osiris.penup()
            osiris.setheading(osirisHeadingStart)
            osiris.goto(osirisCurrentX, osirisCurrentY)            
            if hathor_a == 1: # Determines which side we begin the wings on
                osiris.left(90)
            else:
                osiris.right(90)
            osiris.forward(hathor_span) # How far from the center do we begin
            for hathor_b in range(hathor_no): # How many wings are we going to need
                osiris.penup()
                osirisTemporaryX = osiris.xcor() # Set our center point
                osirisTemporaryY = osiris.ycor() # Set our center point
                if hathor_a == 1: # What's the angle for each wing
                    osiris.right(hathor_angle)
                else:
                    osiris.left(hathor_angle)
                osiris.forward(hathor_gap) # Whats the gap from the centre point for each wing
                osiris.pendown()
                osiris.forward(hathor_length -
                               (hathor_b*hathor_reduction)) # How long are the wings, how much do we reduce on each round
                osiris.penup()
               
                osiris.goto(osirisTemporaryX, osirisTemporaryY)
                if hathor_a == 1: # Controls the spacing between each wing
                    osiris.right(90-hathor_angle)
                    osiris.forward(hathor_spacing)
                    osiris.left(90-hathor_angle)
                else:
                    osiris.left(90-hathor_angle)
                    osiris.forward(hathor_spacing)
                    osiris.right(90-hathor_angle)           
                osiris.forward(hathor_indent) # Whats the indent between each wing
        osiris.goto(osirisCurrentX, osirisCurrentY)
        osiris.setheading(osirisHeadingStart)
        osiris.forward((hathor_no*hathor_spacing)*2) 


def hedetet(hedetet_y,hedetet_start,hedetet_no,hedetet_size,
            hedetet_width,hedetet_right_y,hedetet_left_y,
            hedetet_line_y,hedetet_pensize,hedetet_color):
    def hedetet_right():
        osiris.right(hedetet_width/2)
        for hedetet_a in range(hedetet_no):
            osiris.pendown()
            osiris.circle(hedetet_size,hedetet_width)
            osiris.circle(-hedetet_size,hedetet_width)
            osiris.penup()
    def hedetet_left():
        osiris.left(hedetet_width/2)
        for hedetet_a in range(hedetet_no):
            osiris.pendown()
            osiris.circle(-hedetet_size,hedetet_width)
            osiris.circle(hedetet_size,hedetet_width)
            osiris.penup()
    if hedetet_y == 1:
        osiris.penup()
        osiris.forward(hedetet_start)
        osiris.pensize(hedetet_pensize)
        osiris.color(hedetet_color)
        osiris.setheading(osirisHeadingStart)
        osirisxret = osiris.xcor() 
        osirisyret = osiris.ycor()
        if hedetet_right_y == 1:
            hedetet_right()
            osirisCurrentX = osiris.xcor() 
            osirisCurrentY = osiris.ycor()
        osiris.goto(osirisxret,osirisyret)
        osiris.setheading(osirisHeadingStart)
        if hedetet_left_y == 1:
            hedetet_left()
            osirisCurrentX = osiris.xcor() 
            osirisCurrentY = osiris.ycor()
        osiris.goto(osirisxret,osirisyret)
        if hedetet_line_y == 1:
            osiris.pendown()
        osiris.goto(osirisCurrentX, osirisCurrentY)
        osiris.setheading(osirisHeadingStart)
        osiris.penup()



def hef(hef_y=1,hef_no=10,hef_angle_a=0,hef_angle_b=360,
        hef_forward_a=0,hef_forward_b=300,hef_length_a=50,
        hef_length_b=300,hef_pensize=6,hef_pencolor='#FFFFFF',
        hef_fillcolor='#00FF00'):
    if hef_y == 1:
        for hef_a in range(1,(hef_no+1)):
            osiris.goto(0,0)
            osiris.pensize(hef_pensize)
            osiris.pencolor(hef_pencolor)
            osiris.fillcolor(hef_fillcolor)
            osiris.setheading(osirisHeadingStart)
            osiris.left(randint(hef_angle_a,hef_angle_b))
            osiris.forward(randint(hef_forward_a,hef_forward_b))
            osiris.setheading(osirisHeadingStart)
            hef_length = (randint(hef_length_a,hef_length_b))
            osiris.begin_fill()
            osiris.pendown()
            for hef_b in range(1,5):
                osiris.forward(hef_length)
                osiris.right(90)
            osiris.end_fill()
            osiris.penup()


def imhotep(imhotep_y = 1,imhotep_width = 400,imhotep_height = 400,
            imhotep_spike_no = 1,imhotep_row_no = 2,
            imhotep_row_margin_percent = 10,imhotep_middle_buffer_percent=10,
            imhotep_row_buffer = 10, imhotep_downward_length=75,
            imhotep_downward_no=1, imhotep_downward_cols=1,
            imhotep_row_pensize = 2, imhotep_row_color = '#FF3300',
            imhotep_downward_pensize = 2, imhotep_downward_color = '#0033FF',
            imhotep_bounding_pensize = 2, imhotep_bounding_color = '#00FF33',
            imhotep_write_output=1):
    if imhotep_y == 1:
        if (imhotep_downward_no*imhotep_downward_length) <= (imhotep_height):
            ### We need to work out the angles and lengths involved
            ### Essentially, we're building out a series of triangles
            ### So we need pythag and acos

            ### ~~~~~~~ ROW LOGIC ~~~~~~~~ ###
            imhotep_row_x_start = (imhotep_width / 2 )
            ### Margin at the bottom and top of the tile as a percent
            imhotep_row_margin = ((imhotep_width / 2 ) *
                                  (imhotep_row_margin_percent/100))
            ### Buffer between the top rows and bottom rows
            imhotep_middle_buffer = ((imhotep_width / 2 ) *
                                     (imhotep_middle_buffer_percent/100))
            ### How much space in each half of the tile, need to remove
            ### the margin, padding, buffers etc
            imhotep_working_space = (((imhotep_height/2)-imhotep_row_margin-
                                      (imhotep_middle_buffer/2))-
                                     (imhotep_row_buffer*(imhotep_row_no-1)))
            ### We can then use this working space to figure out how tall each spike is
            imhotep_spike_height = ((imhotep_working_space) / imhotep_row_no)
            ### We the space between each row - this is a constant
            imhotep_row_space = (imhotep_working_space / imhotep_row_no)
            ### How wide is each spike (we determine the spike to be both the up
            ### And the down as a whole)
            imhotep_spike_width = (imhotep_width/(imhotep_spike_no*2))
            ### This is the length of the spike line itself
            ### We use pythag here because we already worked out the height of the spike
            ### And the width of the spike
            imhotep_spike_length = pythag(imhotep_spike_width,imhotep_spike_height)
            imhotep_row_y_start = (imhotep_height / 2)
            ### We need to know how to move osiris, so we need ACOS to find out the
            ### bottom angle of the spike
            imhotep_spike_bottom_angle = (work_acos(imhotep_spike_width,
                                                    imhotep_spike_height,
                                                    imhotep_spike_length))
            
            imhotep_spike_top_angle = (180 - 90) - imhotep_spike_bottom_angle

            
            imhotep_slope_width = (imhotep_width / (imhotep_downward_no+
                                                    imhotep_downward_cols))
           
            imhotep_slope_height = ((imhotep_height - (imhotep_downward_length *
                                                      imhotep_downward_no))/
                                    (imhotep_downward_no+1))
           
            imhotep_slope_length = pythag(imhotep_slope_width,imhotep_slope_height)
            imhotep_slope_bottom_angle = (work_acos(imhotep_slope_width,imhotep_slope_height,
                                                    imhotep_slope_length))
            imhotep_slope_top_angle = (180 - 90) - imhotep_slope_bottom_angle

                                          
            ### Draws the bounding box for the tile ###
            osiris.penup()
            osiris.goto(imhotep_row_x_start,-imhotep_row_y_start)
            osiris.pendown()
            osiris.setheading(90)
            osiris.pensize(imhotep_bounding_pensize)
            osiris.pencolor(imhotep_bounding_color)
            for i in range(2):
                osiris.forward  (imhotep_height)
                osiris.left     (90)
                osiris.forward  (imhotep_width)
                osiris.left     (90)
            ### Draws the zig-zag rows ###
            osiris.penup()
            osiris.goto(0,0)
            osiris.setheading(90)
            osiris.goto(-imhotep_row_x_start,(0+(imhotep_middle_buffer/2)))
            osirisReturnX = osiris.xcor()
            osirisReturnY = osiris.ycor()
            osiris.pencolor(imhotep_row_color)
            osiris.pensize(imhotep_row_pensize)
            ### imhotep_f - 1 = top, 2 = bottom ##            
            for imhotep_f in range(1,3):           
                for imhotep_g in range(1, (imhotep_row_no+1)):
                    for imhotep_h in range(1, (imhotep_spike_no+1)):
                        if imhotep_f == 1:
                            osiris.setheading(90)
                            osiris.right(90-imhotep_spike_bottom_angle)
                        else:
                            osiris.setheading(270)
                            osiris.left(90-imhotep_spike_bottom_angle)
                        osiris.pendown()
                        osiris.forward(imhotep_spike_length)
                        osiris.penup()
                        if imhotep_f == 1:
                            osiris.right(180-(imhotep_spike_top_angle*2))
                        else:
                            osiris.left(180-(imhotep_spike_top_angle*2))
                        osiris.pendown()
                        osiris.forward(imhotep_spike_length)
                        osiris.penup()
                    osiris.goto(osirisReturnX,osirisReturnY)
                    if imhotep_f == 1:
                        osiris.setheading(270)
                    else:
                        osiris.setheading(90)
                    osiris.backward(imhotep_row_space+imhotep_row_buffer)
                    osirisReturnX = osiris.xcor()
                    osirisReturnY = osiris.ycor()
                osiris.goto(-imhotep_row_x_start,(0-(imhotep_middle_buffer/2)))
                osirisReturnX = osiris.xcor()
                osirisReturnY = osiris.ycor()
            ### Draws the downward lines ###
            osiris.pensize(imhotep_downward_pensize)
            osiris.pencolor(imhotep_downward_color)                
            for imhotep_m in range(1,3):
                osiris.goto(0,0)
                osiris.setheading(90)
                if imhotep_m == 1:
                    osiris.goto(-imhotep_row_x_start,imhotep_row_y_start)
                else:
                    osiris.goto(imhotep_row_x_start,imhotep_row_y_start)
                osirisReturnX = osiris.xcor()
                osirisReturnY = osiris.ycor()
                for imhotep_n in range(1, (imhotep_downward_cols+1)):
                    osiris.setheading(90)
                    if imhotep_m == 1:
                        osiris.right(180-imhotep_slope_top_angle)
                    else:
                        osiris.left(180-imhotep_slope_top_angle)
                    osiris.pendown()
                    osiris.forward(imhotep_slope_length)
                    for imhotep_o in range (1, (imhotep_downward_no+1)):
                        osiris.setheading(270)
                        osiris.forward(imhotep_downward_length)
                        osiris.setheading(90)
                        if imhotep_m == 1:
                            osiris.right(180-imhotep_slope_top_angle)
                        else:
                            osiris.left(180-imhotep_slope_top_angle)
                        osiris.pendown()
                        osiris.forward(imhotep_slope_length)
                    osiris.penup()
                    osiris.goto(osirisReturnX,osirisReturnY)
                    if imhotep_m == 1:
                        osiris.setheading(0)
                    else:
                        osiris.setheading(180)
                    osiris.forward(imhotep_slope_width)
                    osirisReturnX = osiris.xcor()
                    osirisReturnY = osiris.ycor()
            ### Outputs the input values for the tile ###                    
            if imhotep_write_output == 1:
                osiris.goto(-imhotep_row_x_start,-imhotep_row_y_start)
                for imhotep_write in ['imhotep_width','imhotep_height','imhotep_spike_no',
                                      'imhotep_row_no','imhotep_row_margin_percent',
                                      'imhotep_row_buffer',
                                      'imhotep_middle_buffer_percent','imhotep_downward_length',
                                      'imhotep_downward_no','imhotep_downward_cols']:
                    osiris.setheading(90)
                    osiris.backward(20)
                    osiris.write(imhotep_write)
                osiris.goto(-(imhotep_row_x_start-200),-imhotep_row_y_start)
                for imhotep_write in [imhotep_width,imhotep_height,imhotep_spike_no,
                                      imhotep_row_no,imhotep_row_margin_percent,
                                      imhotep_row_buffer,
                                      imhotep_middle_buffer_percent,imhotep_downward_length,
                                      imhotep_downward_no,imhotep_downward_cols]:
                    osiris.setheading(90)
                    osiris.backward(20)
                    osiris.write(imhotep_write)              
        else:
            print('Downward value too high, will draw outside of tile')
                                   


def kebechet(kebechet_y=1,kebechet_start=50,kebechet_no=12,
             kebechet_distance=75,kebechet_length=100,kebechet_angle=40,
             kebechet_change=10,kebechet_size=3,kebechet_color='#FF4444'):
    if kebechet_y == 1:
        osiris.penup()
        osiris.pensize(kebechet_size)
        osiris.color(kebechet_color)
        osiris.forward(kebechet_start)
        for kebechet.a in range(1,3):
            osirisCurrentX = osiris.xcor()
            osirisCurrentY = osiris.ycor()
            if kebechet.a == 1:
                osiris.right(90)
            else:
                osiris.left(90)
            osiris.forward(kebechet_distance +
                           (((kebechet_distance*2)/kebechet_no)/2))
            for kebechet.b in range(kebechet_no):
                osiris.setheading(osirisHeadingStart)
                if kebechet.a == 1:
                    osiris.left(90)
                else:
                    osiris.right(90)
                osiris.forward((kebechet_distance*2)/kebechet_no)
                osirisxret = osiris.xcor()
                osirisyret = osiris.ycor()
                osiris.setheading(osirisHeadingStart)
                if kebechet.a == 1:
                    osiris.left(kebechet_angle)
                else:
                    osiris.right(kebechet_angle)
                osiris.pendown()
                osiris.forward(kebechet_length +
                               ((kebechet.b+1)*kebechet_change))
                osiris.penup()
                osiris.goto(osirisxret,osirisyret)
                osiris.setheading(osirisHeadingStart)
            osiris.goto(osirisCurrentX, osirisCurrentY)
            osiris.setheading(osirisHeadingStart)        
        osiris.forward((kebechet_length +
                        ((kebechet.b+1)*kebechet_change)))
        osirisCurrentX = osiris.xcor()  
        osirisCurrentY = osiris.ycor()
        


def khepri(khepri_y=1,khepri_no=2,khepri_length=100,
           khepri_density=4,khepri_pensize=1,
           khepri_pencolor='#FF0000',khepri_fillcolor='#FF0000'):    
    if khepri_y == 1:
        def khepri_west():
            osiris.setheading(90)
            osiris.right(120)
            osiris.pendown()
            khepri_fill_y = randint(1,khepri_density)
            if khepri_fill_y > 1:
                osiris.begin_fill()
            for khepri_f in range(1,4):
                osiris.forward(khepri_length)
                osiris.left(120)
            if khepri_fill_y > 1:
                osiris.end_fill()
            osiris.penup()
        def khepri_east():
            osiris.pendown()
            khepri_fill_y = randint(1,khepri_density)
            if khepri_fill_y > 1:
                osiris.begin_fill()
            for khepri_g in range(1,4):
                osiris.forward(khepri_length)
                osiris.right(120)
            if khepri_fill_y > 1:
                osiris.end_fill()
            osiris.penup()
        osiris.pensize(khepri_pensize)
        osiris.pencolor(khepri_pencolor)
        osiris.fillcolor(khepri_fillcolor)
        khepri_x = (eq_triangle_height(khepri_length) *
                    ((khepri_no+1)/2))
        khepri_y = ((khepri_length/2) * (khepri_no-1))
        osiris.goto(-khepri_x,khepri_y)       
        for khepri_a in range(1,(khepri_no+2)):
            for khepri_e in range(1,(khepri_no+1)):
                if khepri_e == 1:
                    osirisReturnX = osiris.xcor()
                    osirisReturnY = osiris.ycor()            
                khepri_west()
                khepri_east()
                osiris.right(60)
                osiris.forward(khepri_length)
            if khepri_a % 2 == 0:
                khepri_west()
                osiris.goto(osirisReturnX, osirisReturnY)
                osiris.forward(khepri_length)
            else:
                osiris.goto(osirisReturnX, osirisReturnY)
                osiris.setheading(90)
                khepri_east()
                osiris.right(60)
                osiris.forward(khepri_length)



def khnum(khnum_y,khnum_start,khnum_length,
          khnum_gap,khnum_no,khnum_space,
          khnum_reduction,khnum_penreduction,
          khnum_pensize,khnum_color):
    if khnum_y == 1:
        osiris.penup()
        osiris.color(khnum_color)
        for khnum_a in range (1,3):
            osiris.goto(osirisStartingX,osirisStartingY)
            osiris.setheading(osirisHeadingStart)  
            osiris.forward(khnum_start + khnum_length)
            if khnum_a == 1:
                osiris.right(90)
            else:
                osiris.left(90)
            osiris.forward(khnum_gap)
            if khnum_a == 1:
                osiris.right(90)
            else:
                osiris.left(90)
            for khnum_b in range (khnum_no):
                osirisxret = osiris.xcor()
                osirisyret = osiris.ycor()    
                osiris.pensize(khnum_pensize -
                               (khnum_penreduction*(khnum_b+1)))
                osiris.pendown()
                osiris.forward(khnum_length-
                               (khnum_reduction*(khnum_b+1)))
                osiris.penup()
                osiris.goto(osirisxret,osirisyret)
                if khnum_a == 1:
                    osiris.left(90)
                else:
                    osiris.right(90)
                osiris.forward(khnum_space)
                if khnum_a == 1:
                    osiris.right(90)
                else:
                    osiris.left(90)
        osiris.goto(osirisStartingX,osirisStartingY)
        osiris.setheading(osirisHeadingStart)          
            
        


def khonsu(khonsu_y,khonsu_size,khonsu_no,
           khonsu_fill_color):
    def khonsu_star():
        osiris.setheading(60)
        osiris.pendown()
        osiris.begin_fill()
        for khonsu_a in range(1,7):
            osiris.forward(khonsu_size)
            osiris.right(120)
            osiris.forward(khonsu_size)
            osiris.left(60)
        osiris.end_fill()
        osiris.penup()  
    def khonsu_shape():
        osiris.setheading(60)
        osiris.goto(osirisxret,osirisyret)
        osiris.left(60)
        osiris.forward(khonsu_size)
        khonsu_star()
        osiris.setheading(60)
        osiris.penup()
        for khonsu_b in range(1,7):
            osiris.goto(osirisxret,osirisyret)
            osiris.forward(khonsu_size*2)
            osiris.right(60)
            osiris.pendown()
            osiris.begin_fill()
            ##
            ## Draw the legs
            for khonsu_c in range (1,4):
                osiris.forward(khonsu_size*2)
                for khonsu_d in range(1,3):
                    osiris.right(60)
                    osiris.forward(khonsu_size*4)
                osiris.left(60)
                osiris.forward(khonsu_size*3)
                osiris.left(120)
                osiris.forward(khonsu_size)             
                osiris.left(60)
            osiris.penup()
            osiris.end_fill()
        ##Start to draw the two extra stars
        osiris.setheading(60)
        osiris.forward(khonsu_size*8)
        osiris.left(60)
        osiris.forward(khonsu_size*2)
        khonsu_star()
        osiris.setheading(60)
        osiris.left(180)
        osiris.forward(khonsu_size*16)
        osiris.left(60)
        osiris.forward(khonsu_size*6)
        khonsu_star()    
        osiris.setheading(60)
        osiris.goto(osirisxret,osirisyret)
        osiris.forward(khonsu_size*19)
        osiris.left(120)
        osiris.forward(khonsu_size*14)
        osiris.right(120)       
    if khonsu_y == 1:
        khonsu_start_x = (((14 * khonsu_size) * khonsu_no)/4)
        khonsu_start_y = (((20 * khonsu_size) * khonsu_no)/4)
        osiris.goto(-khonsu_start_x,-khonsu_start_y)
        osiris.fillcolor(khonsu_fill_color)
        osirisTemporaryX = osiris.xcor()
        osirisTemporaryY = osiris.ycor()
        osirisxret = osiris.xcor()
        osirisyret = osiris.ycor()
            ##Controls the amount of legs
        for khonsu_j in range(khonsu_no):
            for khonsu_k in range(khonsu_no):
                khonsu_shape()
                osirisxret = osiris.xcor()
                osirisyret = osiris.ycor()
            osiris.goto(osirisTemporaryX, osirisTemporaryY)
            osiris.setheading(60)
            ## Move forward for the next khonsu shape
            ## Need to work out of it is an odd or even column
            ## So that we can move up and down accordingly to balance it out
            if (khonsu_j+1) % 2 == 0:
                osiris.forward(khonsu_size*19)
            else:
                osiris.forward(khonsu_size*14)
            osiris.right(120)
            if (khonsu_j+1) % 2 == 0:
                osiris.forward(khonsu_size*5)    
            else:
                osiris.forward(khonsu_size*19)    
            osirisxret = osiris.xcor()
            osirisyret = osiris.ycor()
            osirisTemporaryX = osiris.xcor()
            osirisTemporaryY = osiris.ycor()


    
def kuk(kuk_y,kuk_start,kuk_no,kuk_angle,
        kuk_depth,kuk_gap,kuk_pensize,kuk_color):
    if kuk_y == 1:
        osiris.penup()
        osiris.forward(kuk_start)
        osiris.pensize(kuk_pensize)
        osiris.color(kuk_color)
        osirisxret = osiris.xcor()
        osirisyret = osiris.ycor()
        for kuk.a in range (1,3):
            for kuk.b in range (kuk_no):
                osiris.penup()
                osiris.goto(osirisxret, osirisyret)
                osiris.setheading(osirisHeadingStart)
                osiris.forward(10 * kuk.b)
                kuk_length = kuk_depth - (20 * kuk.b)
                # sets where the diamonds sit
                osiris.forward((kuk_length*2)*kuk_gap)
                if kuk.b == 0:
                    osirisCurrentX = osiris.xcor()  
                    osirisCurrentY = osiris.ycor()
                osiris.right(180)
                if kuk.a == 1:
                    osiris.left(kuk_angle)
                else:
                    osiris.right(kuk_angle)
                osiris.pendown()
                osiris.forward(kuk_length)
                if kuk.a == 1:
                    osiris.right(kuk_angle*2)
                else:
                    osiris.left(kuk_angle*2)
                osiris.forward(kuk_length)
                if kuk.b == 0:
                    osiris.goto(osirisCurrentX, osirisCurrentY)     
        osiris.penup()
        osiris.goto(osirisCurrentX, osirisCurrentY)
        osiris.setheading(osirisHeadingStart)
        osiris.forward(kuk_length*0.5)




  
def maat(maat_y,maat_start,maat_no,maat_gap,
         maat_vert_increase,maat_bar_size,
         maat_bar_angle,maat_bar_decrease,
         maat_wing_angle,maat_wing_angle_increase,
         maat_wing_length,maat_wing_increase,
         maat_pensize,maat_color):
    if maat_y == 1:
        osiris.forward(maat_start)
        osiris.pensize(maat_pensize)
        osiris.color(maat_color)
        osiris.penup()
        osirisxret = osiris.xcor()
        osirisyret = osiris.ycor()  
        for maat_m in range(1,3):
            for maat_a in range (1,(maat_no+1)):
                osiris.goto(osirisxret, osirisyret)
                osiris.setheading(osirisHeadingStart)
                #Span between each bar
                osiris.forward(maat_vert_increase * maat_a) 
                if maat_m == 1:
                    osiris.right(90)
                    #Whats the gap between the right and left side?
                    osiris.forward(maat_gap) 
                    osiris.setheading(osirisHeadingStart)
                    #Turn around and decide which way the bar points
                    osiris.left(180+maat_bar_angle)          
                else:
                    osiris.left(90)
                    #Whats the gap between the right and left side?
                    osiris.forward(maat_gap)                    
                    osiris.setheading(osirisHeadingStart)
                    #Turn around and decide which way the bar points     
                    osiris.right(180+maat_bar_angle)          
                osiris.pendown()
                osiris.forward(maat_bar_size-
                               (maat_bar_decrease*maat_a)) #Bar size
                if maat_m == 1:
                    osiris.right(maat_wing_angle +
                                 (maat_wing_angle_increase *
                                  maat_a)) #Angle of the wing
                else:
                    osiris.left(maat_wing_angle +
                                (maat_wing_angle_increase
                                 * maat_a)) #Angle of the wing
                osiris.forward(maat_wing_length +
                               (maat_wing_increase *
                                maat_a)) # Size of the wing
                osiris.penup()
        osiris.goto(osirisxret, osirisyret)
        osiris.setheading(osirisHeadingStart)
        osiris.forward(maat_vert_increase * maat_no)
          



def mafdet(mafdet_y,mafdet_start,mafdet_no,mafdet_length,
           mafdet_vert_increase,mafdet_spacing,mafdet_angle,
           mafdet_side_increase,mafdet_pensize,mafdet_color):
    if mafdet_y == 1:
        osiris.penup()
        osiris.forward(mafdet_start)
        osiris.pensize(mafdet_pensize)
        osiris.color(mafdet_color)
        osirisCurrentX = osiris.xcor()
        osirisCurrentY = osiris.ycor()
        for mafdet_a in range(1,3):
            for mafdet_b in range (mafdet_no):
                osiris.goto(osirisCurrentX, osirisCurrentY)
                osiris.setheading(osirisHeadingStart)
                mafdet_length_act = (mafdet_length +
                                     (mafdet_vert_increase
                                      *mafdet_b))
                osiris.forward((mafdet_length_act*2)
                               *mafdet_spacing) 
                if mafdet_a == 1:
                    osiris.right(180)
                    osiris.left(mafdet_angle)
                else:
                    osiris.left(180)
                    osiris.right(mafdet_angle)
                osiris.pendown()
                osiris.forward(mafdet_length_act-
                               (mafdet_side_increase
                                *mafdet_b))
                if mafdet_a == 1:
                    osiris.right(mafdet_angle*2)
                else:
                    osiris.left(mafdet_angle*2)
                osiris.forward(mafdet_length_act-
                               (mafdet_side_increase
                                *mafdet_b))
                osiris.penup()
        osiris.goto(osirisCurrentX, osirisCurrentY)
        osiris.setheading(osirisHeadingStart)
        osiris.forward((mafdet_length_act*2)
                       *mafdet_spacing)
        

def pakhet(pakhet_y=1,pakhet_start=20,pakhet_no=2,pakhet_inner_no=4,
                       pakhet_inner_no_increase=2,pahket_angle_difference=12,
                       pakhet_gap=10,pakhet_length=100,pakhet_length_increase=10,
                       pakhet_outer_y=1,pakhet_outer_space=1.1,pakhet_main_pensize=4,
                       pakhet_inner_pensize=1,pakhet_outline_pensize=2,pakhet_color='#FF4444'):
    if pakhet_y == 1:
        pakhet_angle_1 = 90 - pahket_angle_difference
        pakhet_angle_2 = 90 + pahket_angle_difference
        pakhet_start_angle = (180 - pakhet_angle_2)/2        
        osiris.color(pakhet_color)
        osiris.penup()
        # Draw the main rhombus
        osiris.setheading(osirisHeadingStart)
        osiris.forward(pakhet_start)
        osirisTemporaryX = osiris.xcor()
        osirisTemporaryY = osiris.ycor()
        for pakhet_e in range(1,(pakhet_no+1)):
            osiris.right(pakhet_start_angle)
            osiris.pendown()
            osiris.pensize(pakhet_main_pensize)
            osiris.begin_fill()
            osiris.fillcolor('#FFFFFF')
            for pakhet_f in range(1,3):
                osiris.forward(pakhet_length)
                osiris.left(pakhet_angle_1)
                osiris.forward(pakhet_length)
                osiris.left(pakhet_angle_2)
                if pakhet_f == 1:
                    osirisCurrentX = osiris.xcor()
                    osirisCurrentY = osiris.ycor()
                osirisTemporaryX = osiris.xcor()
                osirisTemporaryY = osiris.ycor()
            osiris.end_fill()
            osiris.penup()
            ## Draw the outer stroke
            if pakhet_outer_y == 1:
                pakhet_middle = (osiris.distance(osirisCurrentX,osirisCurrentY)/2)                
                osiris.setheading(osirisHeadingStart)
                osiris.forward(pakhet_middle)
                osiris.backward(pakhet_middle*pakhet_outer_space)
                osiris.pendown()
                osiris.right(pakhet_start_angle)
                osiris.pensize(pakhet_outline_pensize)
                for pakhet_f in range(1,3):
                    osiris.forward(pakhet_length*pakhet_outer_space)
                    osiris.left(pakhet_angle_1)
                    osiris.forward(pakhet_length*pakhet_outer_space)
                    osiris.left(pakhet_angle_2)
                osiris.penup()
            ## Draw the inner lines
            osiris.pensize(pakhet_inner_pensize)
            for pakhet_g in range(1,3):
                osiris.goto(osirisTemporaryX,osirisTemporaryY)
                for pakhet_h in range(1,(pakhet_inner_no+1)):
                    osiris.setheading(osirisHeadingStart)
                    if pakhet_g == 1:
                        osiris.right(pakhet_start_angle)
                    if pakhet_g == 2:
                        osiris.left(pakhet_start_angle)
                    osiris.forward(pakhet_length/(pakhet_inner_no+1))
                    osirisReturnX = osiris.xcor()
                    osirisReturnY = osiris.ycor()
                    if pakhet_g == 1:
                        osiris.left(pakhet_angle_1)
                    if pakhet_g == 2:
                        osiris.right(pakhet_angle_1)
                    osiris.pendown()
                    osiris.forward(pakhet_length)
                    osiris.penup()
                    osiris.goto(osirisReturnX,osirisReturnY)
            osiris.goto(osirisCurrentX,osirisCurrentY)
            osiris.setheading(osirisHeadingStart)
            osiris.forward(pakhet_gap)
            pakhet_length = pakhet_length + pakhet_length_increase
            pakhet_inner_no = pakhet_inner_no + pakhet_inner_no_increase



         

def ptah(ptah_y,ptah_start,ptah_no,
         ptah_size_a,ptah_size_b,
         ptah_pensize,ptah_color):    
    if ptah_y == 1:
        osiris.penup()
        osiris.forward(ptah_start)
        osiris.pensize(ptah_pensize)
        osiris.color(ptah_color)
        osirisCurrentX = osiris.xcor()
        osirisCurrentY = osiris.ycor()
        for ptah_a in range(ptah_no):
            osiris.goto(osirisCurrentX, osirisCurrentY)
            osiris.pendown()
            osiris.left(78)
            osiris.forward(randint(ptah_size_a,ptah_size_b))
            osiris.penup()
        osiris.penup()
        osiris.goto(osirisCurrentX, osirisCurrentY)    
        osiris.setheading(osirisHeadingStart)
        osiris.forward(ptah_size_b)



def ra(ra_y,ra_angle_a,ra_angle_b,ra_circle_a,
       ra_circle_b,ra_pensize_a,ra_pensize_b,ra_colour): 									
    if ra_y == 1:
        osiris.penup()							
        osiris.pencolor(ra_colour)
        osiris.pensize(randint(ra_pensize_a,
                               ra_pensize_b))			
        osiris.goto(0,0)						
        osiris.right(randint(ra_angle_a,
                             ra_angle_b))			
        osiris.forward(sia)					
        osiris.left(90)	
        osiris.pendown()# Get ready to draw
        # Draw a circle the same size as we moved forward
        osiris.circle(sia, randint(ra_circle_a,
                                   ra_circle_b))	
        osiris.penup()




def raet(raet_y,raet_no,raet_forward,raet_line_y,
         raet_dot_y,raet_dot_no,raet_dot_reduction,
         raet_reduction,raet_pensize,raet_color):
    if raet_y == 1:
        osiris.forward(raet_forward)
        osiris.left(90)
        osiris.penup()
        osiris.color(raet_color)
        osiris.pensize(raet_pensize)
        for raet_a in range(1,(raet_no+1)):
            raet_dot_span = 360 / raet_dot_no
            if raet_line_y == 1:
                osiris.goto(0,0)
                osiris.setheading(90)
                osiris.forward(raet_forward)
                osiris.left(90)
                osiris.pendown()
                osiris.circle(raet_forward)
                osiris.penup()
                raet_forward = raet_forward - raet_reduction
            if raet_dot_y == 1:
                ####
                osiris.goto(0,0)
                osiris.setheading(90)
                osiris.forward(raet_forward)
                osiris.left(90)
                for raet_c in range(1,(raet_dot_no+1)):
                    osiris.circle(raet_forward,raet_dot_span)
                    osiris.dot(5)
                raet_forward = raet_forward - raet_reduction
            raet_dot_no = raet_dot_no - raet_dot_reduction
        if raet_line_y == 1:
            osiris.goto(0,0)
            osiris.setheading(90)
            osiris.forward(raet_forward)
            osiris.left(90)
            osiris.pendown()
            osiris.circle(raet_forward)
            osiris.penup()
            raet_forward = raet_forward - raet_reduction
            


def renenutet(renenutet_y,renenutet_start,renenutet_no,
              renenutet_span,renenutet_forward,
              renenutet_decrease,renenutet_gap,
              renenutet_pensize,renenutet_color):
    if renenutet_y == 1:
        osiris.penup()
        osiris.forward(renenutet_start)
        osiris.pensize(renenutet_pensize)
        osiris.color(renenutet_color)
        osirisCurrentX = osiris.xcor()
        osirisCurrentY = osiris.ycor()
        for renenutet_a in range(1,3):
            osiris.goto(osirisCurrentX, osirisCurrentY)
            osiris.setheading(osirisHeadingStart)     
            for renenutet_b in range(renenutet_no):
                # Turn either left or right to draw the lines
                if renenutet_a == 1:     
                    osiris.right(90)
                else:
                    osiris.left(90)
                osirisTemporaryX = osiris.xcor() # Set our center point
                osirisTemporaryY = osiris.ycor() # Set our center point
                if renenutet_a == 2:
                    if renenutet_b == (renenutet_no-1):
                        osirisCurrentX = osiris.xcor()
                        osirisCurrentY = osiris.ycor()
                osiris.forward(renenutet_span) # Leave a gap if needed
                osiris.pendown()
                # Draw our lines - decreasing if neccessary
                osiris.forward(renenutet_forward-
                               (renenutet_decrease
                                *renenutet_b)) 
                osiris.penup()
                # Return to the center
                osiris.goto(osirisTemporaryX, osirisTemporaryY) 
                if renenutet_a == 1:               
                    osiris.left(90)
                else:
                    osiris.right(90)
                osiris.forward(renenutet_gap) # Move up to the next line
        osiris.goto(osirisCurrentX, osirisCurrentY)
        osirisCurrentX = osiris.xcor()
        osirisCurrentY = osiris.ycor()
        osiris.setheading(osirisHeadingStart)     




def safekh(safekh_y,safekh_size,
           safekh_pensize,safekh_color,sia):
    if safekh_y == 1:
        osiris.penup()
        osiris.pencolor(safekh_color)
        osiris.pensize(safekh_pensize)
        osiris.goto(0,0)
        osiris.setheading(osirisHeadingStart)
        osiris.forward(sia)
        osiris.left(90)
        safekh_decision = 1
        safekh_no = round((10*sia) / safekh_size)
        for safekh_a in range(safekh_no):
            if safekh_decision == 1:
                safekh_penupdown = randint(1,2)
            else:
                safekh_penupdown = 2        
            if safekh_penupdown == 1:
                osiris.pendown()
                safekh_decision = 0
            else:
                osiris.penup()
                safekh_decision = 1
            osiris.circle(sia, (360/safekh_no))
            if safekh_penupdown == 1:
                osiris.penup()
            else:
                osiris.pendown()
        osiris.penup()



def serket(serket_y=1,serket_start=50,serket_angle=25,
           serket_angle_for_outer=35,serket_outer_length=40,
           serket_increase=30,serket_no=10,
           serket_inner_pensize=1,serket_outer_pensize=3,
           serket_pencolor='#FF0900'):
    if serket_y == 1:
        
        serket_back_angle = (180 - 90 -
                             serket_angle)
        
        serket_new_angle = (180 - serket_angle_for_outer -
                            serket_back_angle)
        ## Now we need to work out the opposite angle
        serket_output_angle = (180 - (serket_angle_for_outer*2) -
                            serket_new_angle)
        osiris.penup()
        osiris.goto(osirisStartingX, osirisStartingY)
        osiris.setheading(osirisHeadingStart)
        osiris.forward(serket_start)
        osiris.pencolor(serket_pencolor)
        osirisReturnX = osiris.xcor()
        osirisReturnY = osiris.ycor()
        for serket_a in range (1,3):
            osiris.pensize(serket_inner_pensize)
            serket_outer_length_actual = serket_outer_length
            for serket_m in range(1,(serket_no+1)):
                serket_horizontal = (work_sin
                                     (serket_outer_length_actual,
                                      serket_angle))
                serket_height_from_hor = (work_tan_opp
                                          (serket_horizontal,
                                           serket_angle_for_outer))
                serket_down_length = (pythag
                                      (serket_horizontal,
                                       serket_height_from_hor))

                if serket_a == 1:
                    osiris.left(serket_angle)
                    osiris.forward(serket_outer_length_actual)
                else:
                    osiris.right(serket_angle)
                    osiris.forward(serket_outer_length_actual)
                if serket_a == 1:
                    osiris.right(90+serket_angle)
                    osiris.left(serket_angle_for_outer)
                else:
                    osiris.left(90+serket_angle)
                    osiris.right(serket_angle_for_outer)
                osiris.pendown()
                osiris.forward(serket_down_length)
                osirisCurrentX = osiris.xcor()
                osirisCurrentY = osiris.ycor()                
                # Get in position for going back up
                osiris.setheading(osirisHeadingStart)
                if serket_a == 1:
                    osiris.left(90 - serket_angle_for_outer)
                else:
                    osiris.right(90 - serket_angle_for_outer)
                serket_back_length = (work_sin_opp
                                      (serket_output_angle,
                                       serket_new_angle,
                                       serket_down_length))
                osiris.forward(serket_back_length)
                osiris.penup()
                osirisTemporaryX = osiris.xcor()
                osirisTemporaryY = osiris.ycor()
                if serket_m == serket_no:
                    osiris.pensize(serket_outer_pensize)
                    osiris.pendown()
                osiris.goto(osirisReturnX,osirisReturnY)
                osiris.penup()
                osiris.setheading(osirisHeadingStart)
                serket_outer_length_actual = (serket_outer_length_actual +
                                       serket_increase)


def seshat(seshat_y,seshat_dashes,
           seshat_pensize,seshat_color,sia):
    if seshat_y == 1:
        osiris.penup()
        osiris.pencolor(seshat_color)
        osiris.pensize(seshat_pensize)
        osiris.goto(0,0)
        osiris.setheading(osirisHeadingStart)
        osiris.forward(sia)
        osiris.left(90)
        seshat_decision = 1 
        for seshat_a in range(seshat_dashes):
            if seshat_decision == 1:
                seshat_penupdown = randint(1,2)
            else:
                seshat_penupdown = 2        
            if seshat_penupdown == 1:
                osiris.pendown()
                seshat_decision = 0
            else:
                osiris.penup()
                seshat_decision = 1
            osiris.circle(sia, (360/seshat_dashes))
            if seshat_penupdown == 1:
                osiris.penup()
            else:
                osiris.pendown()
        osiris.penup()



def seth(seth_y,seth_no,seth_angle_a,
         seth_angle_b,seth_span,seth_dist_a,
         seth_dist_b,seth_circle_a,seth_circle_b,
         seth_pensize,seth_color):
    if seth_y == 1:
        for seth_a in range(seth_no):
            osiris.pensize(seth_pensize)
            osiris.pencolor(seth_color)
            osiris.penup()
            # Pick a random angle to start
            osiris.right(randint(seth_angle_a,seth_angle_b))
            # Move forward from the center - if needed
            ##        osiris.forward          (seth_span) 
            osiris.pendown()
            # we need a universal line length
            seth_measurement = (randint
                                (seth_dist_a,seth_dist_b)) 
            osiris.forward(seth_measurement) 
            osiris.right(270)      
            osiris.circle(seth_measurement,
                          randint(seth_circle_a,seth_circle_b)) 
            osiris.goto(0,0)
            osiris.penup()
            


def sobek(sobek_y,sobek_start,sobek_angle,sobek_span,
          sobek_forward,sobek_no,sobek_pensize,sobek_color):    
    if sobek_y == 1:
        osiris.penup()
        osiris.pensize(sobek_pensize)
        osiris.color(sobek_color)
        osiris.setheading(osirisHeadingStart)
        osiris.forward(sobek_start)
        osirisCurrentX = osiris.xcor()
        osirisCurrentY = osiris.ycor()
        osirisReturnX = osiris.xcor()
        osirisReturnY = osiris.ycor()
        osirisTemporaryX = osiris.xcor()
        osirisTemporaryY = osiris.ycor()
        # Draw the arrows
        for sobek_l in range(1,3):
            for sobek_m in range(1,(sobek_no+1)):    
                osiris.setheading(osirisHeadingStart)
                osiris.forward(sobek_span)
                osirisReturnX = osiris.xcor()
                osirisReturnY = osiris.ycor()
                if sobek_l == 1:
                    osiris.right(sobek_angle)
                else:
                    osiris.left(sobek_angle)
                osiris.pendown()
                osiris.forward(sobek_forward)
                osiris.penup()
                osiris.goto(osirisReturnX, osirisReturnY)
            osiris.goto(osirisCurrentX, osirisCurrentY)
        # Draw the parallel lines
        osiris.setheading(osirisHeadingStart)
        osiris.forward(sobek_span*3)
        osirisCurrentX = osiris.xcor()
        osirisCurrentY = osiris.ycor()
        for sobek_n in range(1,3):
            osirisReturnX = osiris.xcor()
            osirisReturnY = osiris.ycor()
            for sobek_p in range(1,(round((sobek_no+1)/2))):
                osiris.setheading(osirisHeadingStart)
                if sobek_n == 1:
                    osiris.right(90)
                else:
                    osiris.left(90)
                osiris.pendown()
                osiris.forward(sobek_forward*0.866)
                osiris.penup()
                osiris.goto(osirisReturnX, osirisReturnY)
                osiris.setheading(osirisHeadingStart)
                osiris.forward(sobek_span*2)
                osirisReturnX = osiris.xcor()
                osirisReturnY = osiris.ycor()
            osiris.goto(osirisCurrentX, osirisCurrentY)
        osiris.goto(osirisTemporaryX, osirisTemporaryY)
        osiris.pendown()
        osiris.goto(osirisReturnX, osirisReturnY)


def sopdu(sopdu_y,sopdu_no,sopdu_distance,
          sopdu_angle,sopdu_forward,sopdu_increase,
          sia_range,sopdu_pensize,sopdu_color):
    if sopdu_y == 1:
        osiris.pensize(sopdu_pensize)
        osiris.color(sopdu_color)
        for sopdu_b in range(sopdu_no):				
            osiris.setheading(osirisHeadingStart)        
            osiris.penup()
            osiris.goto(0,0)
            osiris.right((sopdu_b * (360/sopdu_no))+
                         (sia_range*sopdu_angle))
            osiris.forward(sopdu_distance + sia)
            osiris.pendown()
            osiris.left(sopdu_angle)
            osiris.forward(sopdu_forward+
                           (sia_range*sopdu_increase))
            osiris.right(sopdu_angle/4)
            osiris.forward(sopdu_forward+
                           (sia_range*sopdu_increase))



def thoth(
    thoth_y=1,thoth_height=500,thoth_ray_no_min = 1,
    thoth_ray_no_max = 4,thoth_ray_reverse_no_min = 1,
    thoth_ray_reverse_no_max = 4,thoth_stripe_no_min = 1,
    thoth_stripe_no_max = 4,thoth_stripe_reverse_no_min = 1,
    thoth_stripe_reverse_no_max = 4,thoth_halo_no_min = 1,
    thoth_halo_no_max = 4,thoth_circle_no_min = 1,
    thoth_circle_no_max = 4, 
    thoth_ray_pensize = 2,thoth_ray_color = '#990000',
    thoth_ray_reverse_pensize = 2,thoth_ray_reverse_color = '#990000',
    thoth_stripe_pensize = 2,thoth_stripe_color = '#990000',
    thoth_stripe_reverse_pensize = 2,thoth_stripe_reverse_color = '#990000',
    thoth_halo_pensize = 2,thoth_halo_color = '#990000',
    thoth_circle_pensize = 2,thoth_circle_color = '#990000' 
    ):
    if thoth_y == 1:
        thoth_ray_y = (randint(0,1))    
        thoth_ray_reverse_y = (randint(0,1))    
        thoth_stripe_y = (randint(0,1))    
        thoth_stripe_reverse_y = (randint(0,1))
        thoth_halo_y = (randint(0,1))    
        thoth_circle_y = (randint(0,1))
        thoth_ray_no = (randint(thoth_ray_no_min,thoth_ray_no_max))
        thoth_ray_reverse_no = (randint(thoth_ray_reverse_no_min,thoth_ray_reverse_no_max))
        thoth_stripe_no = (randint(thoth_stripe_no_min,thoth_stripe_no_max))
        thoth_stripe_reverse_no = (randint(thoth_stripe_reverse_no_min,thoth_stripe_reverse_no_max))
        thoth_halo_no = (randint(thoth_halo_no_min,thoth_halo_no_max))
        thoth_circle_no = (randint(thoth_circle_no_min,thoth_circle_no_max))
        thoth_cell_height = thoth_height / 2
        thoth_ray_height = thoth_cell_height / thoth_ray_no
        thoth_ray_reverse_height = thoth_cell_height / thoth_ray_reverse_no     
        thoth_stripe_height = thoth_cell_height / thoth_stripe_no
        thoth_stripe_reverse_height = thoth_cell_height / thoth_stripe_reverse_no        
        thoth_halo_size = thoth_cell_height / thoth_halo_no
        thoth_circle_size = thoth_cell_height / thoth_circle_no
        # Outer Stroke
        osiris.goto(-thoth_cell_height,thoth_cell_height)
        osiris.setheading(270)
        for thoth_box_range in range(1,5):
            osiris.pendown()
            osiris.forward(thoth_height)
            osiris.left(90)
            osiris.penup()
        ### Inner Circles            
        if thoth_circle_y == 1:
            osiris.pensize(thoth_circle_pensize)
            osiris.color(thoth_circle_color)
            for thoth_circle_a in range(1,(thoth_circle_no+1)):
                osiris.goto(0,0)
                osiris.setheading(90)
                osiris.forward(thoth_circle_size*thoth_circle_a)
                osiris.left(90)
                thoth_circle_on_off = (randint(0,1))
                if thoth_circle_on_off == 1:
                    osiris.pendown()
                    osiris.circle((thoth_circle_size*thoth_circle_a),360)
                    osiris.penup()
        ### Outer Circles
        if thoth_halo_y == 1:
            osiris.pensize(thoth_halo_pensize)
            osiris.color(thoth_halo_color)            
            for thoth_halo_range in range(1,(thoth_halo_no+1)):
                thoth_halo_on_off = (randint(0,1))
                thoth_halo_start_heading = 0
                for thoth_halo_a in [(-thoth_cell_height,thoth_cell_height),
                                     (-thoth_cell_height,-thoth_cell_height),
                                     (thoth_cell_height,-thoth_cell_height),
                                     (thoth_cell_height,thoth_cell_height)
                                     ]:
                    osiris.goto(thoth_halo_a)
                    osiris.setheading(thoth_halo_start_heading)
                    osiris.forward(thoth_halo_size*thoth_halo_range)
                    osiris.right(90)
                    if thoth_halo_on_off == 1:
                        osiris.pendown()
                        osiris.circle(-(thoth_halo_size*thoth_halo_range),90)
                        osiris.penup()
                    thoth_halo_start_heading = thoth_halo_start_heading + 90
        ### RAYS FROM THE CENTRE ###
        if thoth_ray_y == 1:
            osiris.pensize(thoth_ray_pensize)
            osiris.color(thoth_ray_color)            
            osiris.goto(0,0)
            osiris.setheading(90)
            for thoth_ray_range in range(0,(thoth_ray_no+1)):
                thoth_ray_on_off = (randint(0,1))        
                for thoth_ray_a in range(1,5):
                    thoth_C = pythag(thoth_cell_height,(thoth_ray_height
                                                        *thoth_ray_range))
                    thoth_M = (work_acos(thoth_cell_height,
                                         (thoth_ray_height*
                                          thoth_ray_range),thoth_C))
                    osiris.left(thoth_M)
                    if thoth_ray_on_off == 1:
                        osiris.pendown()
                        osiris.forward(thoth_C)
                        osiris.penup()
                    osiris.goto(0,0)
                    osiris.left(90-(thoth_M*2)) # We're getting him to turn from the current line to the next liine
                    if thoth_ray_on_off == 1:
                        if 1 <= thoth_ray_range <= (thoth_ray_no-1):
                            osiris.pendown()
                            osiris.forward(thoth_C)
                            osiris.penup()
                            osiris.goto(0,0)
                    osiris.left(thoth_M)
        ### RAYS FROM THE CORNER ###
        if thoth_ray_reverse_y == 1:
            osiris.pensize(thoth_ray_reverse_pensize)
            osiris.color(thoth_ray_reverse_color)
            for thoth_reverse_ray_range in range(0,(thoth_ray_reverse_no+1)):
                thoth_heading = 0
                thoth_reverse_ray_on_off = (randint(0,1))   
                for thoth_x in [(-thoth_cell_height,thoth_cell_height),
                                (-thoth_cell_height,-thoth_cell_height),
                                (thoth_cell_height,-thoth_cell_height),
                                (thoth_cell_height,thoth_cell_height)
                                ]:
                    osiris.goto(thoth_x)
                    osiris.setheading(thoth_heading)           
                    thoth_Q = pythag(thoth_cell_height,(thoth_ray_reverse_height*
                                                        thoth_reverse_ray_range))
                    thoth_P = work_acos(thoth_cell_height,
                                        (thoth_ray_reverse_height*
                                         thoth_reverse_ray_range),thoth_Q)
                    osiris.right(thoth_P)
                    if thoth_reverse_ray_on_off == 1:
                        osiris.pendown()
                        osiris.forward(thoth_Q)
                        osiris.penup()
                    osiris.goto(thoth_x)
                    osiris.right(90-(thoth_P*2))
                    if thoth_reverse_ray_on_off == 1:
                        if thoth_reverse_ray_range <= (thoth_ray_reverse_no-1):
                            osiris.pendown()
                            osiris.forward(thoth_Q)
                            osiris.penup()
                    thoth_heading = thoth_heading + 90
        ### STRIPE FROM THE CENTRE ###
        if thoth_stripe_y == 1:
            osiris.pensize(thoth_stripe_pensize)
            osiris.color(thoth_stripe_color)
            osiris.goto(0,0)
            osiris.setheading(90)
            for thoth_stripe_range in range(1,(thoth_stripe_no+1)):
                thoth_stripe_on_off = (randint(0,1))        
                for thoth_zz in range(1,5):
                    thoth_D_working = thoth_stripe_height * thoth_stripe_range
                    thoth_F = pythag(thoth_D_working,thoth_D_working)
                    osiris.forward(thoth_cell_height-thoth_D_working)
                    osiris.left(45)
                    if thoth_stripe_on_off == 1:            
                        osiris.pendown()
                        osiris.forward(thoth_F)
                        osiris.penup()
                    osiris.goto(0,0)
                    osiris.left(45)
                    osiris.forward(thoth_cell_height-thoth_D_working)
                    osiris.right(45)
                    if thoth_stripe_on_off == 1:
                        if thoth_stripe_range <= (thoth_stripe_no-1):
                            osiris.pendown()
                            osiris.forward(thoth_F)
                            osiris.penup()
                    osiris.goto(0,0)
                    osiris.left(45)
        ### STRIPE FROM THE CORNER ###                    
        if thoth_stripe_reverse_y == 1:
            osiris.pensize(thoth_stripe_reverse_pensize)
            osiris.color(thoth_stripe_reverse_color)
            osiris.goto(0,0)
            thoth_heading = 180
            for thoth_stripe_reverse_range in range(1,(thoth_stripe_reverse_no+1)):
                thoth_stripe_on_off = (randint(0,1))
                for thoth_z in [(0,thoth_cell_height),
                                (-thoth_cell_height,0),
                                (0,-thoth_cell_height),
                                (thoth_cell_height,0)
                                ]:
                    thoth_E_working = (thoth_stripe_reverse_height
                                       * thoth_stripe_reverse_range)
                    thoth_R = pythag(thoth_E_working,thoth_E_working)
                    osiris.goto(thoth_z)
                    osiris.setheading(thoth_heading)  
                    osiris.forward(thoth_cell_height-thoth_E_working)
                    osiris.left(45)
                    if thoth_stripe_on_off == 1:            
                        osiris.pendown()
                        osiris.forward(thoth_R)
                        osiris.penup()
                    if thoth_stripe_reverse_range <= (thoth_stripe_reverse_no-1):
                        osiris.goto(0,0)
                        osiris.setheading(thoth_heading)  
                        osiris.forward(thoth_E_working)
                        osiris.right(135)
                        if thoth_stripe_on_off == 1:            
                            osiris.pendown()
                            osiris.forward(thoth_R)
                            osiris.penup()            
                    thoth_heading = thoth_heading + 90




def wadjwer(wadjwer_y):
    if wadjwer_y == 1:
        osiris.pencolor         ('#FF0000')
        osiris.penup            ()
        osiris.goto             (4000,-4000)
        osiris.pendown          ()
        osiris.setheading       (90)
        for i in range(4):
                osiris.forward  (8000)
                osiris.left     (90)

osiris.speed(2)
def osirisslow():
    osiris.speed(1)
def osirismid():
    osiris.speed(4)
##def osirissuper():
##    osiris.speed(7)
def osirisquick():
    osiris.speed(0)
turtle.onkey(osirisquick,"0")
##turtle.onkey(osirissuper,"7")
turtle.onkey(osirismid,"4")
turtle.onkey(osirisslow,"1")
turtle.listen()
osiris.penup()
osiris.setheading(90)
osirisHeadingStart = osiris.heading()
osiris.goto(0,0)


imhotep(imhotep_y = 0,imhotep_width = 500,imhotep_height = 500,
        imhotep_spike_no = 4,imhotep_row_no = 3,
        imhotep_row_margin_percent = 60,imhotep_middle_buffer_percent=-20,
        imhotep_row_buffer = -100, imhotep_downward_length=20,
        imhotep_downward_no=3, imhotep_downward_cols=4,
        imhotep_row_pensize = 2, imhotep_row_color = '#0033FF',
        imhotep_downward_pensize = 2, imhotep_downward_color = '#0033FF',
        imhotep_bounding_pensize = 2, imhotep_bounding_color = '#0033FF',
        imhotep_write_output=1)
                                      
### KHEPRI      ### ISOMETRIC RANDOM TILES
khepri(khepri_y=0,khepri_no=7,khepri_length=25,
       khepri_density=3,khepri_pensize=0,
       khepri_pencolor='#FF0000',khepri_fillcolor='#00FFC0')


khonsu(0,20,2,'#40CCFF')
    

apep(0,300,0,0,0,5,1,'#000000','#000000')


bennu(0,300,0,0,0,5,1,'#000000','#000000')



thoth(
    thoth_y=0,thoth_height=500,thoth_ray_no_min = 1,
    thoth_ray_no_max = 4,thoth_ray_reverse_no_min = 1,
    thoth_ray_reverse_no_max = 4,thoth_stripe_no_min = 1,
    thoth_stripe_no_max = 4,thoth_stripe_reverse_no_min = 1,
    thoth_stripe_reverse_no_max = 4,thoth_halo_no_min = 1,
    thoth_halo_no_max = 4,thoth_circle_no_min = 1,
    thoth_circle_no_max = 4, 
    thoth_ray_pensize = 2,thoth_ray_color = '#990000',
    thoth_ray_reverse_pensize = 2,thoth_ray_reverse_color = '#990000',
    thoth_stripe_pensize = 2,thoth_stripe_color = '#990000',
    thoth_stripe_reverse_pensize = 2,thoth_stripe_reverse_color = '#990000',
    thoth_halo_pensize = 2,thoth_halo_color = '#990000',
    thoth_circle_pensize = 2,thoth_circle_color = '#990000' 
    )


amun(0,12,0,180,150,800,4,'#FF1493')


anubis(0,3,400,40,0,14,6,1,14,8,3,3,'#90CC16')

geb(geb_y=0,geb_no=13,geb_circum_a=10,geb_circum_b=250,
    geb_distance_a=50,geb_distance_b=400,
    geb_circle_reduction_a=5,geb_circle_reduction_b=75,
    geb_pensize=3,geb_pencolor='#0000FF',geb_fillcolor='#FF0000')

### HEF         ### RANDOM SQUARES
hef(hef_y=0,hef_no=12,hef_angle_a=0,hef_angle_b=360,
    hef_forward_a=0,hef_forward_b=300,hef_length_a=50,
    hef_length_b=300,hef_pensize=6,hef_pencolor='#FFFFFF',
    hef_fillcolor='#00FF00')

raet(0,4,300,1,1,30,5,30,3,'#2F92CC')


seth(0,10,0,270,0,30,300,5,100,1,'#1234FF') 


shai                    = 100
sia                     = shai

for sia_range in range(1,30): 
      

    sopdu(1,12,50,120,30,10,sia_range,2,'#FF3456')


    ra(1,0,360,120,360,1,4,'#7800FF')


    seshat(1,40,2,'#001493',sia)


    safekh(1,80,2,'#001493',sia)
    sia = sia + shai # NO NEED TO CHANGE THIS (EVER)


shu = 0

osiris.setheading(90)
for shu_a in range(shu):
    osiris.penup()             
    osiris.goto(0,0)
    osiris.forward(0)   
    osirisHeadingStart = osiris.heading()  
    osirisStartingX = osiris.xcor()
    osirisStartingY = osiris.ycor()

    apedemak(apedemak_y=0,apedemak_start=0,
             apedemak_span_angle=70,apedemak_spike_inner_angle= 60,
             apedemak_length = 400,apedemak_spike_no = 5,
             apedemak_little_spike = 1,apedemak_little_spike_type = 'percentage',
             apedemak_little_spike_reduction = 0.5,adepemak_slash_space = 0.5,
             adepemak_slash_extension = 200,adepemak_slash_no = 3,
             apedemak_spike_pensize = 4,apedemak_spike_color = '#FF4400',
             apedemak_little_spike_pensize = 3,
             apedemak_little_spike_color = '#FF4499',
             apedemak_slash_pensize = 6,apedemak_slash_color = '#4444FF')

### SERKET        ### CONE WITH CRISS CROSS LINES
    serket(serket_y=0,serket_start=0,serket_angle=20,
           serket_angle_for_outer=35,serket_outer_length=100,
           serket_increase=20,serket_no=21,
           serket_inner_pensize=1,serket_outer_pensize=3,
           serket_pencolor='#FF0900')
    
### Make sure we reset the position
    osiris.goto(osirisStartingX,osirisStartingY)
    osiris.setheading(osirisHeadingStart)


    bast(0,0,30,120,1,4,'#004444',osirisStartingX,osirisStartingY)

### Make sure we reset the position
    osiris.goto(osirisStartingX,osirisStartingY)
    osiris.setheading(osirisHeadingStart)

### HAPI        ### CROSS OVER LINES - VERTICAL
    hapi(hapi_y=0,hapi_start=0,hapi_length=1000,
         hapi_angle=-30,hapi_line_no=7,hapi_section_no=3,
         hapi_space=10,hapi_pensize=2,hapi_color='#FF3333')

### Make sure we reset the position
    osiris.goto(osirisStartingX,osirisStartingY)
    osiris.setheading(osirisHeadingStart)    

    khnum(0,0,600,100,30,10,0,0,4,'#6544FF')

    osiris.goto(osirisStartingX,osirisStartingY)
    osiris.setheading(osirisHeadingStart)

    aker(aker_y=0,aker_span=-10,aker_start=150,
         aker_start_increase = 8,aker_no=6,aker_length=550,
         aker_length_increase=-30,aker_angle=12,aker_angle_increase=5,
         aker_gap=5,aker_gap_increase=3,aker_pensize=2,aker_color='#0FC200')


    amunet(0,50,200,9,'#FF4444') 

 
    anhur(0,50,9,380,28,5,'#00FF00')


    anput(0,50,1,100,4,1,'#FF4444')


    aten(0,50,100,10,8,90,300,1,3,'#901273')
   

    hathor(0,50,0,50,200,8,140,15,15,10,2,'#FF4444')


    hedetet(0,50,1,100,100,0,1,1,4,'#F012EE')

    kebechet(kebechet_y=0,kebechet_start=125,kebechet_no=16,
             kebechet_distance=150,kebechet_length=200,kebechet_angle=45,
             kebechet_change=-10,kebechet_size=3,kebechet_color='#FF4444')
    

    kuk(0,0,5,40,200,0.86,3,'#FF4444')


    maat(0,50,10,0,20,200,45,5,200,10,200,20,2,'#F778AA') 


    mafdet(0,-20,14,150,10,0.70,45,20,2,'#004444')


    ptah(0,100,10,20,300,2,'#FF4444')          


    pakhet(pakhet_y=0, pakhet_start=0, pakhet_no=2, pakhet_inner_no=2,
           pakhet_inner_no_increase=3, pahket_angle_difference=0,
           pakhet_gap=0, pakhet_length=50, pakhet_length_increase=50,
           pakhet_outer_y=0, pakhet_outer_space=1.1, pakhet_main_pensize=6,
           pakhet_inner_pensize=1, pakhet_outline_pensize=2, pakhet_color='#FF4444')

  
    renenutet(0,50,15,10,250,15,10,5,'#FF4444')
    osiris.goto(osirisStartingX,osirisStartingY)
    osiris.setheading(osirisHeadingStart)
   
 
    sobek(0,-25,45,26,150,30,4,'#F7A120')  
    


    osiris.setheading(osirisHeadingStart)
    osirisHeadingStart = osirisHeadingStart + (360/shu)
    osiris.setheading(osirisHeadingStart)



wadjwer(0)djwer_y

turtle.done()

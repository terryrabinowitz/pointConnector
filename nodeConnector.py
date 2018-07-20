import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import random
import numpy as np


def user_input():
    print "Enter number of nodes"
    num_nodes = int(raw_input())
    print "Enter max X value"
    max_x = int(raw_input())
    print "Enter max Y value"
    max_y = int(raw_input())
    return num_nodes, max_x, max_y


def ccw(xa,ya,xb,yb,xc,yc):
    return (yc-ya) * (xb-xa) > (yb-ya) * (xc-xa)

# Return true if line segments AB and CD intersect
def intersect(xa,ya,xb,yb,xc,yc,xd,yd):
    return ccw(xa,ya,xc,yc,xd,yd) != ccw(xb,yb,xc,yc,xd,yd) and ccw(xa,ya,xb,yb,xc,yc) != ccw(xa,ya,xb,yb,xd,yd)


def line_cross_check(x,y):
    for i in range(len(x)-2):
        for j in range(i+2,len(x)):
            if (j+1) != len(x):
                xa = x[i]
                ya = y[i]
                xb = x[i + 1]
                yb = y[i + 1]
                xc = x[j]
                yc = y[j]
                xd = x[j + 1]
                yd = y[j + 1]
            elif i!=0:
                xa = x[i]
                ya = y[i]
                xb = x[i + 1]
                yb = y[i + 1]
                xc = x[j]
                yc = y[j]
                xd = x[0]
                yd = y[0]
            fail_check = intersect(xa,ya,xb,yb,xc,yc,xd,yd)
            print fail_check




def node_one_past(delta_x, delta_y):
    past = []
    choice_random = random.randint(1,3)
    if delta_x[0] > 0 and delta_y[0] > 0:
        if choice_random == 1:
            past.append(('0','+'))
        elif choice_random == 2:
            past.append(('+','+'))
        elif choice_random == 3:
            past.append(('+','0'))
    elif delta_x[0] > 0 and delta_y[0] == 0:
        if choice_random == 1:
            past.append(('+','+'))
        elif choice_random == 2:
            past.append(('+','0'))
        elif choice_random == 3:
            past.append(('+','-'))
    elif delta_x[0] > 0 and delta_y[0] < 0:
        if choice_random == 1:
            past.append(('+','0'))
        elif choice_random == 2:
            past.append(('+','-'))
        elif choice_random == 3:
            past.append(('0','-'))
    elif delta_x[0] == 0 and delta_y[0] < 0:
        if choice_random == 1:
            past.append(('+', '-'))
        elif choice_random == 2:
            past.append(('0', '-'))
        elif choice_random == 3:
            past.append(('-', '-'))
    elif delta_x[0] < 0 and delta_y[0] < 0:
        if choice_random == 1:
            past.append(('0', '-'))
        elif choice_random == 2:
            past.append(('-', '-'))
        elif choice_random == 3:
            past.append(('-', '0'))
    elif delta_x[0] < 0 and delta_y[0] == 0:
        if choice_random == 1:
            past.append(('-', '-'))
        elif choice_random == 2:
            past.append(('-', '0'))
        elif choice_random == 3:
            past.append(('-', '+'))
    elif delta_x[0] < 0 and delta_y[0] > 0:
        if choice_random == 1:
            past.append(('-', '0'))
        elif choice_random == 2:
            past.append(('-', '+'))
        elif choice_random == 3:
            past.append(('0', '+'))
    elif delta_x[0] == 0 and delta_y[0] > 0:
        if choice_random == 1:
            past.append(('-', '+'))
        elif choice_random == 2:
            past.append(('0', '+'))
        elif choice_random == 3:
            past.append(('+', '+'))
    return past


def node_one_slopes(past, l_transform, r_transform):
    m_ref = []
    m_unit = []
    choice_random = random.uniform(0.001,10)
    if past[0] == ('+', '+'):
        m_ref.append(choice_random)
    elif past[0] == ('+', '0'):
        m_ref.append(0.0)
    elif past[0] == ('+', '-'):
        m_ref.append(-1* choice_random)
    elif past[0] == ('0', '-'):
        m_ref.append(np.inf)
    elif past[0] == ('-', '-'):
        m_ref.append(choice_random)
    elif past[0] == ('-', '0'):
        m_ref.append(0.0)
    elif past[0] == ('-', '+'):
        m_ref.append(-1* choice_random)
    elif past[0] == ('0', '+'):
        m_ref.append(np.inf)
    if m_ref[0] == np.inf and r_transform[0] == -1:
        m_unit.append(0.0)
    elif m_ref[0] == 0.0 and r_transform[0] == -1:
        m_unit.append(np.inf)
    elif m_ref[0] == np.inf and r_transform[0] == 1:
        m_unit.append(np.inf)
    elif m_ref[0] == 0.0 and r_transform[0] == 1:
        m_unit.append(0.0)
    else:
        m_unit.append(l_transform[0] * (m_ref[0] / r_transform[0])**r_transform[0])
    return m_ref, m_unit


def node_one_curve(m_ref, m_line, l_transform, r_transform):
    n_ref = []
    n_unit = []
    curve_type = []
    return curve_type, n_unit, n_ref


def initialize(num_nodes, max_x, max_y):
    x = []
    y = []
    for i in range(num_nodes):
        x.append(random.uniform(-1 * max_x, max_x))
        y.append(random.uniform(-1 * max_y, max_y))
    # x = [0,0.1,2.2,2.9]
    # y = [0,1.1,2.7,0.15]
    delta_x = []
    delta_y = []
    m_line = []
    l_transform = []
    r_transform = []
    for i in range(1, num_nodes):
        delta_x.append((x[i] - x[i-1]))
        delta_y.append((y[i] - y[i-1]))
        m_line.append(float(delta_y[i-1]) / delta_x[i-1])
        l_transform.append(np.absolute(float(delta_x[i-1]) / delta_y[i-1]))
        if (delta_x[i-1] >= 0 and delta_y[i-1] >=0) or (delta_x[i-1] <= 0 and delta_y[i-1] <=0):
            r_transform.append(1.0)
        else:
            r_transform.append(-1.0)
    delta_x.append((x[0] - x[num_nodes-1]))
    delta_y.append((y[0] - y[num_nodes-1]))
    m_line.append(float(delta_y[num_nodes-1])/delta_x[num_nodes-1])
    l_transform.append(np.absolute(float(delta_x[num_nodes-1])/delta_y[num_nodes-1]))
    if (delta_x[num_nodes-1] >= 0 and delta_y[num_nodes-1] >= 0) or (delta_x[num_nodes-1] <= 0 and delta_y[num_nodes-1] <= 0):
        r_transform.append(1.0)
    else:
        r_transform.append(-1.0)
    past = node_one_past(delta_x, delta_y)
    m_ref, m_unit = node_one_slopes(past, l_transform, r_transform)
    return x, y, delta_x, delta_y, m_line, m_ref, m_unit, l_transform, r_transform, past


def plot_initial(max_x, max_y, x, y):
    plt.plot(x, y, 'o', mfc='r',mec='r',markersize=2)
    plt.xlim(-2*max_x, 2*max_x)
    plt.ylim(-2*max_y, 2*max_y)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Node Connecter')
    plt.draw()
    plt.pause(1)


def curve_equation(index, x, y, delta_x, delta_y, l_transform, r_transform, m_unit, n_unit, curve_type):
        n_ref = r_transform[index] * (n_unit / l_transform[index]) ** r_transform[index]
        m_ref = r_transform[index] * (m_unit / l_transform[index]) ** r_transform[index]
        print n_ref, m_ref
        a = np.linspace(x[index], x[index + 1], 1000)
        if curve_type == 1 or curve_type ==2:
            b = y[index] + delta_y[index] * ((a-x[index]) / delta_x[index]) ** n_ref
        elif curve_type == 3 or curve_type == 4:
            b = y[index] + delta_y[index] * (1-(1-(a - x[index]) / delta_x[index]) ** m_ref)
        elif curve_type == 5 or curve_type == 6:
            b = y[index] + delta_y[index] * (1-(1-(a - x[index]) / delta_x[index]) ** m_ref)**(1/m_ref)
        elif curve_type == 7 or curve_type == 8:
            denominator =((n_ref**2/(n_ref+1)**2)-(m_ref**2/(m_ref+1)**2))
            b = y[index] + delta_y[index] * ((1-(1-((1-1/(n_ref+1)**2) - (1-1/(m_ref+1)**2))
                * ((a - x[index]) / delta_x[index])-(1-1/(m_ref+1)**2))**.5)**2
                - (1-(1-(1-1/(m_ref+1)**2))**.5)**2) / denominator
        return a,b


def plot_connect(index, x, y, delta_x, delta_y, l_transform, r_transform, m_unit, n_unit, curve_type):
    a,b = curve_equation(index, x, y, delta_x, delta_y, l_transform, r_transform, m_unit, n_unit, curve_type)
    plt.plot(a, b, 'o', mfc='b', mec = 'b', color='b', ls='solid', markersize=2)
    plt.plot(x[index], y[index], 'o', mfc='g', mec='g', markersize=2)
    plt.pause(3)


def main():
    num_nodes, max_x, max_y = user_input()
    x, y, delta_x, delta_y, m_line, m_ref, m_unit, l_transform, r_transform, past = initialize(num_nodes, max_x, max_y)
    if num_nodes > 3:
        line_cross_check(x,y)


    plot_initial(max_x, max_y, x, y)
    #curve_type, n_unit, n_ref = node_one_curve(m_ref, m_line, l_transform, r_transform)
    curve_type = 7
    m_unit = 2.0
    n_unit = 0.5
    for index in range(num_nodes-1):
        plot_connect(index, x, y, delta_x, delta_y, l_transform, r_transform, m_unit, n_unit, curve_type)


plt.ion()
fig = plt.figure()
ax = fig.gca()
main()
plt.pause(100000)


#need line cross check
#need node insert
#need curve_type from appendix
#need last node to first node connect (optional)
    #lock first an last coordinate
#load coordinates
#allow smooth and sharp transitions
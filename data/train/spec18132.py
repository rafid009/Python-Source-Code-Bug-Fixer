import numpy as np 

def function(x):

	t1 = x
	g4 = x
	paths = []
	try:
		if t1 > 3:
			t1 = t1+t1
			g4 = x/g4
			x = x+9
			paths.append(1)
		else:
			x = g4*0
			g4 = g4/1
			x = 4-0
			paths.append(2)
		if x > 5:
			t1 = t1*4
			g4 = t1*1
			paths.append(3)
		else:
			x = x*8
			g4 = 5*x
			t1 = 7/t1
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		t1 = t1**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
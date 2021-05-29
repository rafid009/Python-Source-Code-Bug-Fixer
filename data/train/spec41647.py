import numpy as np 

def function(x):

	l0 = 1
	t9 = x
	paths = []
	try:
		if x <= 8:
			x = x/7
			x = 7+l0
			paths.append(1)
		else:
			l0 = l0/l0
			l0 = 5-l0
			paths.append(2)
		if t9 <= 0:
			x = x-1
			l0 = 0*l0
			t9 = t9-2
			paths.append(3)
		else:
			x = x*2
			l0 = l0+t9
			t9 = t9/2
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		t9 = t9**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
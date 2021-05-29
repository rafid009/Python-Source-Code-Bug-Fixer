import numpy as np 

def function(x):

	l0 = x
	t5 = x
	paths = []
	try:
		if l0 < 6:
			x = x*5
			paths.append(1)
		else:
			l0 = l0*l0
			paths.append(2)
		if l0 <= 8:
			t5 = 1*t5
			t5 = l0*t5
			t5 = 5-t5
			paths.append(3)
		else:
			t5 = 1*0
			t5 = l0-x
			l0 = 8*3
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		x = t5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
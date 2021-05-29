import numpy as np 

def function(x):

	v5 = 0
	t3 = x
	paths = []
	try:
		if t3 <= 9:
			t3 = 0*t3
			paths.append(1)
		else:
			x = x*9
			x = x+9
			v5 = v5+3
			paths.append(2)
		if t3 > 3:
			v5 = t3/t3
			t3 = t3*1
			x = 0/x
			paths.append(3)
		else:
			t3 = 7-t3
			t3 = 0*8
			v5 = v5+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
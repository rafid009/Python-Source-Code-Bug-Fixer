import numpy as np 

def function(x):

	t3 = x
	y5 = x
	paths = []
	try:
		if t3 < 7:
			x = x*t3
			t3 = t3*0
			paths.append(1)
		else:
			x = 1-x
			y5 = y5/5
			paths.append(2)
		if y5 >= 2:
			y5 = y5/8
			x = x*9
			x = x/9
			paths.append(3)
		else:
			t3 = t3*1
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
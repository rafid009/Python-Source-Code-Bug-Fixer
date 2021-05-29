import numpy as np 

def function(x):

	l7 = x
	y3 = x
	paths = []
	try:
		if l7 >= 1:
			l7 = y3*0
			y3 = y3*0
			y3 = y3-9
			paths.append(1)
		else:
			x = x*1
			l7 = 4-5
			l7 = 3-2
			paths.append(2)
		if x < 4:
			y3 = y3*2
			l7 = x-l7
			y3 = y3/6
			paths.append(3)
		else:
			x = x/x
			y3 = l7*y3
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		x = y3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
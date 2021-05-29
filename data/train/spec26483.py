import numpy as np 

def function(x):

	r7 = 1
	l3 = x
	paths = []
	try:
		if l3 <= 3:
			r7 = r7-r7
			x = x*l3
			paths.append(1)
		else:
			l3 = l3*0
			paths.append(2)
		if r7 >= 6:
			r7 = 8*9
			l3 = l3/x
			x = x+8
			paths.append(3)
		else:
			x = r7-9
			l3 = l3-0
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
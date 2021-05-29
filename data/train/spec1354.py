import numpy as np 

def function(x):

	q1 = x
	a1 = x
	x = x
	paths = []
	try:
		if a1 <= 4:
			x = x+a1
			q1 = q1+0
			paths.append(1)
		else:
			a1 = a1+2
			x = x-9
			a1 = a1/a1
			paths.append(2)
		if q1 <= 4:
			x = x*0
			paths.append(3)
		else:
			a1 = 3/8
			q1 = q1-0
			q1 = q1/q1
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		x = a1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
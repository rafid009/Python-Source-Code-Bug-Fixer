import numpy as np 

def function(x):

	e1 = 2
	j5 = x
	paths = []
	try:
		if x <= 4:
			e1 = e1/4
			paths.append(1)
		else:
			x = 2-3
			x = 4-8
			j5 = e1*x
			paths.append(2)
		if j5 >= 5:
			e1 = e1/9
			j5 = 7*j5
			e1 = e1+e1
			paths.append(3)
		else:
			x = x+0
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		x = j5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
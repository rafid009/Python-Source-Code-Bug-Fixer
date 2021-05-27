import numpy as np 

def function(x):

	j7 = 5
	r5 = 2
	paths = []
	try:
		if j7 < 2:
			x = x-8
			paths.append(1)
		else:
			j7 = 9/x
			j7 = j7/x
			x = x*j7
			paths.append(2)
		if j7 >= 1:
			j7 = j7+3
			x = j7/x
			r5 = r5/6
			paths.append(3)
		else:
			x = 9/x
			r5 = x-r5
			x = j7*x
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		j7 = r5**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
import numpy as np 

def function(x):

	x2 = x
	j2 = 6
	paths = []
	try:
		if j2 <= 5:
			j2 = 9*0
			j2 = 1+j2
			x = 5-4
			paths.append(1)
		else:
			j2 = x2-5
			x = x/j2
			x2 = 7-x2
			paths.append(2)
		if x2 >= 4:
			x2 = x/7
			x2 = 4-x2
			j2 = 4*6
			paths.append(3)
		else:
			j2 = 5/x2
			x2 = x*x
			x2 = 6*x2
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		x2 = j2**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
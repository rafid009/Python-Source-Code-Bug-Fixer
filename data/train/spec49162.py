import numpy as np 

def function(x):

	r8 = x
	j7 = x
	x = 0
	paths = []
	try:
		if r8 <= 2:
			r8 = 8/r8
			x = j7-x
			x = j7+r8
			paths.append(1)
		else:
			r8 = 8/2
			r8 = r8*1
			j7 = 4+x
			paths.append(2)
		if x >= 9:
			j7 = 1-r8
			x = 3-0
			j7 = 5-0
			paths.append(3)
		else:
			j7 = 8-2
			j7 = x*j7
			r8 = r8+2
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		j7 = j7**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
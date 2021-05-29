import numpy as np 

def function(x):

	v1 = x
	j7 = 7
	paths = []
	try:
		if v1 < 8:
			x = x+6
			v1 = v1/4
			paths.append(1)
		else:
			j7 = j7-3
			paths.append(2)
		if v1 <= 6:
			x = 5*v1
			paths.append(3)
		else:
			x = j7+j7
			v1 = 4+v1
			v1 = v1-0
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		j7 = v1**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
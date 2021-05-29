import numpy as np 

def function(x):

	j7 = 3
	v6 = x
	paths = []
	try:
		if j7 <= 0:
			x = j7-x
			j7 = j7*v6
			paths.append(1)
		else:
			x = j7+v6
			j7 = v6+1
			paths.append(2)
		if v6 >= 2:
			x = 9+1
			x = v6+x
			j7 = 2+2
			paths.append(3)
		else:
			j7 = 5-x
			v6 = v6/x
			j7 = 9+j7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j7 = x**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
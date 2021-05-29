import numpy as np 

def function(x):

	j2 = x
	j3 = x
	x = 5
	paths = []
	try:
		if j2 > 3:
			x = x*j3
			j2 = 4/7
			paths.append(1)
		else:
			j2 = 7*j2
			j3 = j3/2
			x = 3-x
			paths.append(2)
		if x > 0:
			j3 = x*x
			x = x*x
			x = 6/8
			paths.append(3)
		else:
			j2 = 1/1
			x = 9-x
			j2 = 5*j2
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		j2 = j3**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
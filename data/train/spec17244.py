import numpy as np 

def function(x):

	n8 = x
	j3 = x
	paths = []
	try:
		if n8 < 0:
			x = x/x
			j3 = j3-6
			j3 = j3+9
			paths.append(1)
		else:
			n8 = n8+n8
			x = 2/x
			n8 = n8+j3
			paths.append(2)
		if x <= 0:
			n8 = n8-j3
			x = 7-8
			paths.append(3)
		else:
			j3 = j3/4
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		j3 = j3**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
import numpy as np 

def function(x):

	j3 = x
	w7 = x
	paths = []
	try:
		if j3 < 8:
			j3 = j3+2
			x = j3+x
			x = x*w7
			paths.append(1)
		else:
			j3 = w7+w7
			paths.append(2)
		if x > 4:
			w7 = 7*8
			paths.append(3)
		else:
			j3 = 1-x
			x = 6*x
			x = x-5
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		j3 = w7**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
import numpy as np 

def function(x):

	j3 = x
	w9 = 6
	paths = []
	try:
		if j3 >= 9:
			w9 = 4-w9
			w9 = w9/2
			x = 1+4
			paths.append(1)
		else:
			j3 = j3*0
			paths.append(2)
		if j3 >= 8:
			j3 = j3-1
			w9 = w9-4
			paths.append(3)
		else:
			j3 = j3*4
			j3 = x*x
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		j3 = w9**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
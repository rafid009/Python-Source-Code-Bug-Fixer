import numpy as np 

def function(x):

	j2 = 9
	w9 = 9
	paths = []
	try:
		if j2 <= 2:
			x = x-8
			paths.append(1)
		else:
			w9 = w9-4
			paths.append(2)
		if x <= 3:
			x = x*w9
			w9 = j2+x
			j2 = w9*j2
			paths.append(3)
		else:
			j2 = j2+j2
			j2 = w9/8
			j2 = j2+9
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		w9 = j2**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
import numpy as np 

def function(x):

	j2 = x
	w8 = x
	paths = []
	try:
		if x <= 4:
			x = 9/j2
			j2 = 8-6
			paths.append(1)
		else:
			w8 = w8-0
			x = 1+x
			paths.append(2)
		if x > 1:
			w8 = 7+j2
			j2 = j2+6
			w8 = j2*1
			paths.append(3)
		else:
			j2 = x*j2
			x = x*w8
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		x = w8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
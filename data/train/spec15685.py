import numpy as np 

def function(x):

	o8 = x
	j2 = 0
	paths = []
	try:
		if x <= 7:
			j2 = j2+j2
			o8 = x+8
			paths.append(1)
		else:
			o8 = 3/o8
			x = 7*x
			x = x*8
			paths.append(2)
		if o8 <= 5:
			o8 = j2-0
			o8 = 8-6
			j2 = x*j2
			paths.append(3)
		else:
			j2 = x*9
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		x = j2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
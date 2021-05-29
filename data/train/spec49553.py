import numpy as np 

def function(x):

	j2 = 8
	o2 = x
	paths = []
	try:
		if x >= 9:
			o2 = 2*o2
			x = o2*9
			x = x+x
			paths.append(1)
		else:
			o2 = 1-o2
			paths.append(2)
		if j2 >= 4:
			x = j2/x
			j2 = x*j2
			paths.append(3)
		else:
			o2 = 4-o2
			j2 = j2+8
			o2 = x/1
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		o2 = j2**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
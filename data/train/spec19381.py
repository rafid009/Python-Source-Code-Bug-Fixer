import numpy as np 

def function(x):

	i5 = x
	o9 = 1
	paths = []
	try:
		if i5 < 0:
			i5 = i5*i5
			i5 = 2*2
			paths.append(1)
		else:
			o9 = i5*o9
			i5 = 0*o9
			x = 7+x
			paths.append(2)
		if x < 4:
			x = 0/x
			x = 6/9
			paths.append(3)
		else:
			i5 = i5-8
			o9 = 4-o9
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		o9 = i5**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
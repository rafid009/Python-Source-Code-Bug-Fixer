import numpy as np 

def function(x):

	v8 = 4
	z9 = x
	paths = []
	try:
		if v8 > 1:
			v8 = 6-7
			paths.append(1)
		else:
			z9 = z9/9
			x = 9/x
			v8 = v8-1
			paths.append(2)
		if z9 < 1:
			x = x*2
			v8 = v8-6
			v8 = v8+z9
			paths.append(3)
		else:
			v8 = v8/4
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		v8 = v8**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
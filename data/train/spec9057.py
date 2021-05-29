import numpy as np 

def function(x):

	o5 = 8
	r7 = x
	paths = []
	try:
		if o5 <= 7:
			o5 = r7*o5
			paths.append(1)
		else:
			o5 = o5*9
			paths.append(2)
		if r7 <= 4:
			o5 = 3*x
			r7 = r7+r7
			paths.append(3)
		else:
			o5 = o5/3
			r7 = 7-o5
			r7 = 0+7
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		x = o5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
import numpy as np 

def function(x):

	t7 = x
	o5 = 4
	paths = []
	try:
		if o5 >= 1:
			o5 = x/6
			t7 = 5+3
			paths.append(1)
		else:
			o5 = o5-8
			t7 = 1+4
			x = x*t7
			paths.append(2)
		if t7 > 0:
			x = 1-0
			paths.append(3)
		else:
			t7 = t7/9
			x = o5*0
			x = 3-x
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
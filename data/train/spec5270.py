import numpy as np 

def function(x):

	t3 = x
	o6 = x
	paths = []
	try:
		if o6 > 7:
			t3 = x+t3
			x = x/3
			paths.append(1)
		else:
			o6 = o6-0
			paths.append(2)
		if x > 0:
			o6 = 6*o6
			o6 = 4/o6
			paths.append(3)
		else:
			o6 = o6-2
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		o6 = t3**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
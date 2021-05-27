import numpy as np 

def function(x):

	t1 = 5
	o5 = 7
	paths = []
	try:
		if t1 >= 4:
			t1 = t1*x
			t1 = t1*o5
			t1 = t1+6
			paths.append(1)
		else:
			o5 = o5*t1
			paths.append(2)
		if o5 <= 1:
			o5 = o5-2
			x = x/2
			paths.append(3)
		else:
			o5 = o5-o5
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		o5 = t1**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
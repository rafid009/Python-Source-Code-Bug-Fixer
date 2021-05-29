import numpy as np 

def function(x):

	u0 = x
	t5 = x
	x = 5
	paths = []
	try:
		if t5 >= 1:
			u0 = u0+7
			t5 = t5+5
			paths.append(1)
		else:
			u0 = u0-0
			u0 = 0/6
			u0 = u0*0
			paths.append(2)
		if t5 < 8:
			u0 = u0+t5
			x = 5*7
			paths.append(3)
		else:
			u0 = u0-4
			x = x+6
			x = 4/x
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		u0 = t5**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
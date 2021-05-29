import numpy as np 

def function(x):

	u1 = x
	t5 = x
	paths = []
	try:
		if t5 >= 4:
			x = x*x
			x = u1+x
			t5 = t5-9
			paths.append(1)
		else:
			u1 = u1-u1
			u1 = u1-2
			u1 = u1*x
			paths.append(2)
		if t5 <= 8:
			u1 = x*2
			x = x/2
			u1 = x+7
			paths.append(3)
		else:
			t5 = 1*t5
			x = 2/x
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		u1 = u1**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
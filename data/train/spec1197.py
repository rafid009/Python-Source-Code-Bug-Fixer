import numpy as np 

def function(x):

	u1 = x
	t1 = x
	paths = []
	try:
		if u1 >= 7:
			x = x*8
			t1 = t1-8
			paths.append(1)
		else:
			u1 = 3-t1
			u1 = x+u1
			x = t1+x
			paths.append(2)
		if u1 > 3:
			x = x+9
			x = x*3
			u1 = 0*u1
			paths.append(3)
		else:
			t1 = t1+4
			x = 5/x
			t1 = 2-t1
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		u1 = t1**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
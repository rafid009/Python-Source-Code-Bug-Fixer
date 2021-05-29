import numpy as np 

def function(x):

	w2 = x
	u1 = x
	paths = []
	try:
		if u1 >= 2:
			w2 = 5*w2
			w2 = 0*u1
			paths.append(1)
		else:
			w2 = w2+4
			paths.append(2)
		if w2 <= 5:
			u1 = u1*5
			x = x*3
			paths.append(3)
		else:
			w2 = u1+w2
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
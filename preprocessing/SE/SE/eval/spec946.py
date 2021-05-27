import numpy as np 

def function(x):

	u8 = x
	r4 = x
	paths = []
	try:
		if u8 >= 5:
			r4 = x/1
			paths.append(1)
		else:
			u8 = 2*u8
			paths.append(2)
		if r4 < 4:
			x = x/4
			paths.append(3)
		else:
			r4 = 3+r4
			u8 = u8*0
			r4 = 5/9
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		r4 = r4**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
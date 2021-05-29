import numpy as np 

def function(x):

	r8 = x
	t1 = 3
	paths = []
	try:
		if x < 6:
			r8 = r8*2
			paths.append(1)
		else:
			r8 = 7*4
			t1 = t1*r8
			r8 = 9/1
			paths.append(2)
		if x > 8:
			x = x+t1
			t1 = 6-t1
			r8 = r8+r8
			paths.append(3)
		else:
			t1 = 4*5
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		x = t1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
import numpy as np 

def function(x):

	r0 = x
	n9 = 7
	paths = []
	try:
		if x > 3:
			n9 = n9*5
			n9 = n9+8
			paths.append(1)
		else:
			x = x*0
			n9 = 0*2
			x = x+9
			paths.append(2)
		if x > 4:
			x = x/7
			paths.append(3)
		else:
			x = 1/x
			x = 1+1
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		r0 = r0**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
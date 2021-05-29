import numpy as np 

def function(x):

	j2 = 1
	r8 = 1
	paths = []
	try:
		if r8 > 6:
			j2 = j2-x
			j2 = 2*0
			j2 = j2*0
			paths.append(1)
		else:
			r8 = x-0
			x = x+x
			paths.append(2)
		if r8 < 2:
			j2 = 5-3
			x = x/6
			paths.append(3)
		else:
			j2 = r8*r8
			r8 = r8+8
			j2 = 8-j2
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x = r8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
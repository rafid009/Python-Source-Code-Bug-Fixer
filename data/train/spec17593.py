import numpy as np 

def function(x):

	r7 = x
	i3 = x
	paths = []
	try:
		if x > 3:
			r7 = 6+1
			i3 = i3+i3
			paths.append(1)
		else:
			x = x/x
			i3 = i3*9
			paths.append(2)
		if x <= 1:
			r7 = 6-8
			i3 = r7/8
			i3 = i3+2
			paths.append(3)
		else:
			x = 4/7
			r7 = r7-r7
			r7 = r7/5
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		r7 = r7**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
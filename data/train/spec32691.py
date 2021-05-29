import numpy as np 

def function(x):

	r7 = 1
	t7 = 2
	paths = []
	try:
		if r7 <= 6:
			r7 = r7+x
			r7 = 8+x
			t7 = t7*t7
			paths.append(1)
		else:
			x = 2+x
			x = x*9
			paths.append(2)
		if x <= 2:
			r7 = r7-4
			t7 = t7/x
			paths.append(3)
		else:
			x = 6+x
			x = 6-2
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		t7 = r7**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
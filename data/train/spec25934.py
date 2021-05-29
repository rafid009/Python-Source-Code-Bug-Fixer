import numpy as np 

def function(x):

	t3 = x
	i5 = 8
	x = x
	paths = []
	try:
		if i5 >= 6:
			i5 = i5-7
			x = x-7
			i5 = 3+6
			paths.append(1)
		else:
			t3 = 8-t3
			t3 = t3*7
			i5 = i5/5
			paths.append(2)
		if i5 <= 9:
			i5 = 5-i5
			x = x+9
			i5 = i5+x
			paths.append(3)
		else:
			x = x-0
			i5 = 9/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t3 = x**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
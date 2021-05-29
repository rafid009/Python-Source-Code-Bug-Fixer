import numpy as np 

def function(x):

	t8 = 2
	t3 = 1
	paths = []
	try:
		if t8 <= 7:
			x = 3*7
			paths.append(1)
		else:
			x = 5-t8
			t3 = t3/5
			paths.append(2)
		if t8 >= 1:
			t3 = t3-2
			t8 = t8-6
			x = x*1
			paths.append(3)
		else:
			t3 = t3+t3
			x = x*8
			x = t8+1
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		t3 = t8**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
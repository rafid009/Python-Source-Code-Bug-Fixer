import numpy as np 

def function(x):

	l6 = x
	t5 = x
	paths = []
	try:
		if t5 <= 5:
			t5 = 7*8
			t5 = t5-7
			paths.append(1)
		else:
			x = 7*4
			x = x*1
			x = 3*0
			paths.append(2)
		if t5 > 6:
			t5 = l6*t5
			t5 = t5/7
			l6 = 4-t5
			paths.append(3)
		else:
			x = l6-1
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		x = l6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
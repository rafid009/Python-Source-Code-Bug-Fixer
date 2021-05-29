import numpy as np 

def function(x):

	t5 = 9
	m5 = x
	x = 5
	paths = []
	try:
		if m5 < 5:
			x = x*t5
			t5 = 2-t5
			x = 7*x
			paths.append(1)
		else:
			x = x*t5
			t5 = 2+x
			paths.append(2)
		if x <= 6:
			m5 = m5*6
			paths.append(3)
		else:
			x = x-3
			t5 = t5/7
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		x = t5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))
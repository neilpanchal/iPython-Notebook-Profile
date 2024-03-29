# Configuration file for ipython-qtconsole.

c = get_config()

#------------------------------------------------------------------------------
# IPythonQtConsoleApp configuration
#------------------------------------------------------------------------------

# IPythonQtConsoleApp will inherit config from: BaseIPythonApplication,
# Application, IPythonConsoleApp, ConnectionFileMixin

# The name of the default kernel to start.
# c.IPythonQtConsoleApp.kernel_name = 'python'

# Start the console window with the menu bar hidden.
# c.IPythonQtConsoleApp.hide_menubar = False

# Whether to overwrite existing config files when copying
# c.IPythonQtConsoleApp.overwrite = False

# Connect to an already running kernel
# c.IPythonQtConsoleApp.existing = ''

# set the heartbeat port [default: random]
# c.IPythonQtConsoleApp.hb_port = 0

# Path to the ssh key to use for logging in to the ssh server.
# c.IPythonQtConsoleApp.sshkey = ''

# The name of the IPython directory. This directory is used for logging
# configuration (through profiles), history storage, etc. The default is usually
# $HOME/.ipython. This option can also be specified through the environment
# variable IPYTHONDIR.
# c.IPythonQtConsoleApp.ipython_dir = ''

# set the control (ROUTER) port [default: random]
# c.IPythonQtConsoleApp.control_port = 0

# set the shell (ROUTER) port [default: random]
# c.IPythonQtConsoleApp.shell_port = 0

# Set the kernel's IP address [default localhost]. If the IP address is
# something other than localhost, then Consoles on other machines will be able
# to connect to the Kernel, so be careful!
# c.IPythonQtConsoleApp.ip = ''

# The Logging format template
# c.IPythonQtConsoleApp.log_format = '[%(name)s]%(highlevel)s %(message)s'

# Path to an extra config file to load.
# 
# If specified, load this config file in addition to any other IPython config.
# c.IPythonQtConsoleApp.extra_config_file = ''

# The date format used by logging formatters for %(asctime)s
# c.IPythonQtConsoleApp.log_datefmt = '%Y-%m-%d %H:%M:%S'

# set the iopub (PUB) port [default: random]
# c.IPythonQtConsoleApp.iopub_port = 0

# Set the log level by value or name.
# c.IPythonQtConsoleApp.log_level = 30

# Start the console window maximized.
# c.IPythonQtConsoleApp.maximize = False

# Whether to display a banner upon starting the QtConsole.
# c.IPythonQtConsoleApp.display_banner = True

# path to a custom CSS stylesheet
# c.IPythonQtConsoleApp.stylesheet = ''

# set the stdin (ROUTER) port [default: random]
# c.IPythonQtConsoleApp.stdin_port = 0

# Create a massive crash report when IPython encounters what may be an internal
# error.  The default is to append a short message to the usual traceback
# c.IPythonQtConsoleApp.verbose_crash = False

# The SSH server to use to connect to the kernel.
# c.IPythonQtConsoleApp.sshserver = ''

# JSON file in which to store connection info [default: kernel-<pid>.json]
# 
# This file will contain the IP, ports, and authentication key needed to connect
# clients to this kernel. By default, this file will be created in the security
# dir of the current profile, but can be specified by absolute path.
# c.IPythonQtConsoleApp.connection_file = ''

# 
# c.IPythonQtConsoleApp.transport = 'tcp'

# Set to display confirmation dialog on exit. You can always use 'exit' or
# 'quit', to force a direct exit without any confirmation.
# c.IPythonQtConsoleApp.confirm_exit = True

# Whether to install the default config files into the profile dir. If a new
# profile is being created, and IPython contains config files for that profile,
# then they will be staged into the new directory.  Otherwise, default config
# files will be automatically generated.
# c.IPythonQtConsoleApp.copy_config_files = False

# Whether to create profile dir if it doesn't exist
# c.IPythonQtConsoleApp.auto_create = False

# The IPython profile to use.
# c.IPythonQtConsoleApp.profile = 'default'

# Use a plaintext widget instead of rich text (plain can't print/save).
# c.IPythonQtConsoleApp.plain = False

#------------------------------------------------------------------------------
# IPythonWidget configuration
#------------------------------------------------------------------------------

# A FrontendWidget for an IPython kernel.

# IPythonWidget will inherit config from: FrontendWidget, HistoryConsoleWidget,
# ConsoleWidget

# The height of the console at start time in number of characters (will double
# with `vsplit` paging)
# c.IPythonWidget.height = 25

# If not empty, use this Pygments style for syntax highlighting. Otherwise, the
# style sheet is queried for Pygments style information.
# c.IPythonWidget.syntax_style = ''

# Whether to ask for user confirmation when restarting kernel
# c.IPythonWidget.confirm_restart = True

# The type of paging to use. Valid values are:
# 
# 'inside'
#    The widget pages like a traditional terminal.
# 'hsplit'
#    When paging is requested, the widget is split horizontally. The top
#    pane contains the console, and the bottom pane contains the paged text.
# 'vsplit'
#    Similar to 'hsplit', except that a vertical splitter is used.
# 'custom'
#    No action is taken by the widget beyond emitting a
#    'custom_page_requested(str)' signal.
# 'none'
#    The text is written directly to the console.
# c.IPythonWidget.paging = 'inside'

# Whether to process ANSI escape codes.
# c.IPythonWidget.ansi_codes = True

# 
# c.IPythonWidget.out_prompt = 'Out[<span class="out-prompt-number">%i</span>]: '

# The font size. If unconfigured, Qt will be entrusted with the size of the
# font.
# c.IPythonWidget.font_size = 0

# 
# c.IPythonWidget.history_lock = False

# Whether to include output from clients other than this one sharing the same
# kernel.
# 
# Outputs are not displayed until enter is pressed.
# c.IPythonWidget.include_other_output = False

# Whether to draw information calltips on open-parentheses.
# c.IPythonWidget.enable_calltips = True

# The type of underlying text widget to use. Valid values are 'plain', which
# specifies a QPlainTextEdit, and 'rich', which specifies a QTextEdit.
# c.IPythonWidget.kind = 'plain'

# Whether to automatically execute on syntactically complete input.
# 
# If False, Shift-Enter is required to submit each execution. Disabling this is
# mainly useful for non-Python kernels, where the completion check would be
# wrong.
# c.IPythonWidget.execute_on_complete_input = True

# The maximum number of lines of text before truncation. Specifying a non-
# positive number disables text truncation (not recommended).
# c.IPythonWidget.buffer_size = 500

# 
# c.IPythonWidget.output_sep = ''

# The width of the console at start time in number of characters (will double
# with `hsplit` paging)
# c.IPythonWidget.width = 81

# 
# c.IPythonWidget.input_sep = '\n'

# The type of completer to use. Valid values are:
# 
# 'plain'   : Show the available completion as a text list
#             Below the editing area.
# 'droplist': Show the completion in a drop down list navigable
#             by the arrow keys, and from which you can select
#             completion by pressing Return.
# 'ncurses' : Show the completion as a text list which is navigable by
#             `tab` and arrow keys.
# c.IPythonWidget.gui_completion = 'ncurses'

# Whether to clear the console when the kernel is restarted
# c.IPythonWidget.clear_on_kernel_restart = True

# 
# c.IPythonWidget.banner = ''

# A command for invoking a system text editor. If the string contains a
# {filename} format specifier, it will be used. Otherwise, the filename will be
# appended to the end the command.
# c.IPythonWidget.editor = ''

# The editor command to use when a specific line number is requested. The string
# should contain two format specifiers: {line} and {filename}. If this parameter
# is not specified, the line number option to the %edit magic will be ignored.
# c.IPythonWidget.editor_line = ''

# The font family to use for the console. On OSX this defaults to Monaco, on
# Windows the default is Consolas with fallback of Courier, and on other
# platforms the default is Monospace.
# c.IPythonWidget.font_family = ''

# A CSS stylesheet. The stylesheet can contain classes for:
#     1. Qt: QPlainTextEdit, QFrame, QWidget, etc
#     2. Pygments: .c, .k, .o, etc. (see PygmentsHighlighter)
#     3. IPython: .error, .in-prompt, .out-prompt, etc
# c.IPythonWidget.style_sheet = ''

# 
# c.IPythonWidget.output_sep2 = ''

# The pygments lexer class to use.
# c.IPythonWidget.lexer_class = <IPython.utils.traitlets.Undefined object at 0x101542f98>

# 
# c.IPythonWidget.in_prompt = 'In [<span class="in-prompt-number">%i</span>]: '

#------------------------------------------------------------------------------
# KernelManager configuration
#------------------------------------------------------------------------------

# Manages a single kernel in a subprocess on this host.
# 
# This version starts kernels with Popen.

# KernelManager will inherit config from: ConnectionFileMixin

# set the control (ROUTER) port [default: random]
# c.KernelManager.control_port = 0

# set the shell (ROUTER) port [default: random]
# c.KernelManager.shell_port = 0

# Set the kernel's IP address [default localhost]. If the IP address is
# something other than localhost, then Consoles on other machines will be able
# to connect to the Kernel, so be careful!
# c.KernelManager.ip = ''

# set the stdin (ROUTER) port [default: random]
# c.KernelManager.stdin_port = 0

# set the heartbeat port [default: random]
# c.KernelManager.hb_port = 0

# Should we autorestart the kernel if it dies.
# c.KernelManager.autorestart = False

# set the iopub (PUB) port [default: random]
# c.KernelManager.iopub_port = 0

# JSON file in which to store connection info [default: kernel-<pid>.json]
# 
# This file will contain the IP, ports, and authentication key needed to connect
# clients to this kernel. By default, this file will be created in the security
# dir of the current profile, but can be specified by absolute path.
# c.KernelManager.connection_file = ''

# 
# c.KernelManager.transport = 'tcp'

# DEPRECATED: Use kernel_name instead.
# 
# The Popen Command to launch the kernel. Override this if you have a custom
# kernel. If kernel_cmd is specified in a configuration file, IPython does not
# pass any arguments to the kernel, because it cannot make any assumptions about
# the  arguments that the kernel understands. In particular, this means that the
# kernel does not receive the option --debug if it given on the IPython command
# line.
# c.KernelManager.kernel_cmd = []

#------------------------------------------------------------------------------
# ProfileDir configuration
#------------------------------------------------------------------------------

# An object to manage the profile directory and its resources.
# 
# The profile directory is used by all IPython applications, to manage
# configuration, logging and security.
# 
# This object knows how to find, create and manage these directories. This
# should be used by any code that wants to handle profiles.

# Set the profile location directly. This overrides the logic used by the
# `profile` option.
# c.ProfileDir.location = ''

#------------------------------------------------------------------------------
# Session configuration
#------------------------------------------------------------------------------

# Object for handling serialization and sending of messages.
# 
# The Session object handles building messages and sending them with ZMQ sockets
# or ZMQStream objects.  Objects can communicate with each other over the
# network via Session objects, and only need to work with the dict-based IPython
# message spec. The Session will handle serialization/deserialization, security,
# and metadata.
# 
# Sessions support configurable serialization via packer/unpacker traits, and
# signing with HMAC digests via the key/keyfile traits.
# 
# Parameters ----------
# 
# debug : bool
#     whether to trigger extra debugging statements
# packer/unpacker : str : 'json', 'pickle' or import_string
#     importstrings for methods to serialize message parts.  If just
#     'json' or 'pickle', predefined JSON and pickle packers will be used.
#     Otherwise, the entire importstring must be used.
# 
#     The functions must accept at least valid JSON input, and output *bytes*.
# 
#     For example, to use msgpack:
#     packer = 'msgpack.packb', unpacker='msgpack.unpackb'
# pack/unpack : callables
#     You can also set the pack/unpack callables for serialization directly.
# session : bytes
#     the ID of this Session object.  The default is to generate a new UUID.
# username : unicode
#     username added to message headers.  The default is to ask the OS.
# key : bytes
#     The key used to initialize an HMAC signature.  If unset, messages
#     will not be signed or checked.
# keyfile : filepath
#     The file containing a key.  If this is set, `key` will be initialized
#     to the contents of the file.

# Debug output in the Session
# c.Session.debug = False

# The name of the packer for serializing messages. Should be one of 'json',
# 'pickle', or an import name for a custom callable serializer.
# c.Session.packer = 'json'

# Threshold (in bytes) beyond which an object's buffer should be extracted to
# avoid pickling.
# c.Session.buffer_threshold = 1024

# Username for the Session. Default is your system username.
# c.Session.username = 'Neil'

# The name of the unpacker for unserializing messages. Only used with custom
# functions for `packer`.
# c.Session.unpacker = 'json'

# execution key, for signing messages.
# c.Session.key = b''

# The digest scheme used to construct the message signatures. Must have the form
# 'hmac-HASH'.
# c.Session.signature_scheme = 'hmac-sha256'

# Threshold (in bytes) beyond which a buffer should be sent without copying.
# c.Session.copy_threshold = 65536

# path to file containing execution key.
# c.Session.keyfile = ''

# The UUID identifying this session.
# c.Session.session = ''

# The maximum number of items for a container to be introspected for custom
# serialization. Containers larger than this are pickled outright.
# c.Session.item_threshold = 64

# The maximum number of digests to remember.
# 
# The digest history will be culled when it exceeds this value.
# c.Session.digest_history_size = 65536

# Metadata dictionary, which serves as the default top-level metadata dict for
# each message.
# c.Session.metadata = {}

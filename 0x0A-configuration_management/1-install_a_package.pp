# Install puppet-int
package { 'puppet-lint':
  ensure   => '2.5.0',
  provider => 'gem',
}
